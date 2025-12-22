import argparse
import json
from typing import Any

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, context_precision, faithfulness

SAMPLE_DATA = {
    'question': [
        '关于生成式 AI 的局限性是什么？',
        '为什么发布门禁要把阻断级样本单独对待？',
        'RAG 的评测里为什么要关注上下文精度？',
    ],
    'answer': [
        '生成式 AI 的局限性主要包括事实幻觉、安全风险和资源消耗。它可能生成听起来合理但不准确的信息，也可能被用于生成虚假内容；此外训练与推理会消耗大量计算资源。',
        '因为阻断级样本代表不可接受的风险面，例如越权或泄露；它们一旦失败就必须阻断发布，而不是用均值把风险稀释掉。',
        '因为检索喂入的上下文如果信噪比太低，会让模型更容易跑偏或堆砌无关信息；上下文精度能量化检索是否在给答案提供有效证据。',
    ],
    'contexts': [
        [
            '某篇关于生成式 AI 优缺点的文章指出，其局限性包括生成幻觉内容、可能被用于恶意目的以及在训练和运行过程中需要大量计算资源。文章还指出，即使是先进模型也难以完全避免生成不准确或有偏颇的信息。'
        ],
        [
            '发布门禁通常会把越权、泄露、注入等高风险用例设为阻断级：命中即失败，避免用平均分掩盖极端风险。'
        ],
        [
            'RAG 系统的质量不只取决于生成模型，还取决于检索到的上下文是否相关且简洁。上下文精度用于衡量检索内容的相关性与信噪比。'
        ],
    ],
}


def _as_float(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        pass
    if hasattr(value, 'mean'):
        return float(value.mean())
    if isinstance(value, (list, tuple)):
        if not value:
            return 0.0
        return float(sum(value) / len(value))
    raise TypeError(f'unsupported score type: {type(value)}')


def _load_jsonl(path: str) -> dict:
    questions: list[str] = []
    answers: list[str] = []
    contexts: list[list[str]] = []
    with open(path, 'r', encoding='utf-8') as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            questions.append(obj['question'])
            answers.append(obj['answer'])
            contexts.append(obj['contexts'])
    return {'question': questions, 'answer': answers, 'contexts': contexts}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--in',
        dest='input_path',
        default='',
        help='可选：JSONL 输入文件，每行包含 question、answer、contexts',
    )
    parser.add_argument(
        '--threshold-faithfulness',
        '--faithfulness-threshold',
        dest='threshold_faithfulness',
        type=float,
        default=0.85,
    )
    parser.add_argument(
        '--threshold-answer-relevancy',
        '--answer-relevancy-threshold',
        dest='threshold_answer_relevancy',
        type=float,
        default=0.70,
    )
    parser.add_argument(
        '--threshold-context-precision',
        '--context-precision-threshold',
        dest='threshold_context_precision',
        type=float,
        default=0.60,
    )
    args = parser.parse_args()

    data = _load_jsonl(args.input_path) if args.input_path else SAMPLE_DATA
    ds = Dataset.from_dict(data)

    try:
        result = evaluate(ds, metrics=[faithfulness, answer_relevancy, context_precision])
    except Exception as e:
        raise SystemExit(f'RAGAS 评测运行失败：{e}')

    scores = {
        'faithfulness': _as_float(result['faithfulness']),
        'answer_relevancy': _as_float(result['answer_relevancy']),
        'context_precision': _as_float(result['context_precision']),
    }

    print('--- RAGAS 评测报告（均值）---')
    print('faithfulness={:.3f} threshold={:.3f}'.format(scores['faithfulness'], args.threshold_faithfulness))
    print(
        'answer_relevancy={:.3f} threshold={:.3f}'.format(
            scores['answer_relevancy'], args.threshold_answer_relevancy
        )
    )
    print(
        'context_precision={:.3f} threshold={:.3f}'.format(
            scores['context_precision'], args.threshold_context_precision
        )
    )

    failed = False
    if scores['faithfulness'] < args.threshold_faithfulness:
        print('FAIL: faithfulness below threshold')
        failed = True
    if scores['answer_relevancy'] < args.threshold_answer_relevancy:
        print('FAIL: answer_relevancy below threshold')
        failed = True
    if scores['context_precision'] < args.threshold_context_precision:
        print('FAIL: context_precision below threshold')
        failed = True

    if failed:
        raise SystemExit(1)

    print('RAG 门禁通过')


if __name__ == '__main__':
    main()

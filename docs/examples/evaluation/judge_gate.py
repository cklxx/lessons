#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Stats:
    total: int
    a: int
    b: int
    tie: int

    @property
    def a_win_rate(self) -> float:
        return 0.0 if self.total <= 0 else self.a / self.total

    @property
    def tie_rate(self) -> float:
        return 0.0 if self.total <= 0 else self.tie / self.total


def _load_report(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def _stats(report: dict[str, Any]) -> Stats:
    items = report.get('items') or []
    if not isinstance(items, list):
        raise ValueError('invalid report: items must be a list')
    a = b = tie = 0
    for it in items:
        if not isinstance(it, dict):
            continue
        final = str(it.get('final') or '').strip()
        if final == 'A':
            a += 1
        elif final == 'B':
            b += 1
        else:
            tie += 1
    return Stats(total=len(items), a=a, b=b, tie=tie)


def main() -> int:
    parser = argparse.ArgumentParser(description='Gate pairwise judge report against a baseline.')
    parser.add_argument('--baseline', required=True, help='Baseline report JSON from judge_pairwise.py')
    parser.add_argument('--candidate', required=True, help='Candidate report JSON from judge_pairwise.py')
    parser.add_argument('--max-win-rate-drop', type=float, default=0.01)
    parser.add_argument('--max-win-count-drop', type=int, default=1)
    parser.add_argument('--max-tie-rate-increase', type=float, default=0.03)
    parser.add_argument('--max-tie-count-increase', type=int, default=5)
    args = parser.parse_args()

    base = _stats(_load_report(Path(args.baseline)))
    cand = _stats(_load_report(Path(args.candidate)))

    if base.total <= 0 or cand.total <= 0:
        raise SystemExit('empty report')
    if base.total != cand.total:
        raise SystemExit('report size mismatch')

    win_drop = base.a_win_rate - cand.a_win_rate
    win_count_drop = base.a - cand.a
    tie_rate_increase = cand.tie_rate - base.tie_rate
    tie_count_increase = cand.tie - base.tie

    print(
        'baseline: total={} A={} B={} Tie={} a_win_rate={:.3f} tie_rate={:.3f}'.format(
            base.total, base.a, base.b, base.tie, base.a_win_rate, base.tie_rate
        )
    )
    print(
        'candidate: total={} A={} B={} Tie={} a_win_rate={:.3f} tie_rate={:.3f}'.format(
            cand.total, cand.a, cand.b, cand.tie, cand.a_win_rate, cand.tie_rate
        )
    )
    print(
        'delta: win_rate_drop={:.3f} win_count_drop={} tie_rate_increase={:.3f} tie_count_increase={}'.format(
            win_drop, win_count_drop, tie_rate_increase, tie_count_increase
        )
    )

    failed = False
    if win_drop > args.max_win_rate_drop:
        print('FAIL: A win rate dropped too much')
        failed = True
    if win_count_drop > args.max_win_count_drop:
        print('FAIL: A win count dropped too much')
        failed = True
    if tie_rate_increase > args.max_tie_rate_increase:
        print('FAIL: Tie rate increased too much')
        failed = True
    if tie_count_increase > args.max_tie_count_increase:
        print('FAIL: Tie count increased too much')
        failed = True

    if failed:
        return 1

    print('PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

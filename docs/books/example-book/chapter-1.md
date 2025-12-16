# 第一章：开场

欢迎来到第一章！这一节展示了如何在书中编写叙事文字、列表与代码示例。

## 为什么选择 Python

Python 拥有简洁的语法和丰富的社区生态，适合快速验证想法，也适合构建生产系统。

!!! tip "写作建议"
    章节开头放一段背景说明，可以帮助读者进入情境。

## 简单的代码示例

下面的函数演示了如何读取一个 Markdown 文件并统计其中的行数：

```python
from pathlib import Path

def count_lines(path: str) -> int:
    """统计文件行数，若文件不存在则返回 0。"""
    file_path = Path(path)
    if not file_path.exists():
        return 0
    return sum(1 for _ in file_path.read_text(encoding="utf-8").splitlines())

if __name__ == "__main__":
    lines = count_lines("chapter-1.md")
    print(f"本章共 {lines} 行内容")
```

你可以在本地运行这段代码，或者将其替换成你的示例。

## 后续规划

- 添加强化练习，比如小测验或思考题。
- 嵌入图片或流程图解释复杂概念。
- 结合项目实践，展示完整的应用案例。

下一节可以继续展开更多话题，尽情创作吧！

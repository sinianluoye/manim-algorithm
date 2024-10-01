from manim import Paragraph, VGroup, Integer, Dot, DOWN, Code

def index_paragraph_labels(
    paragraph: Paragraph,
    label_height: float = 0.1,
    **kwargs,
):
    labels = VGroup()
    idx = 0
    for i in range(len(paragraph)):
        if not isinstance(paragraph[i], Dot): 
            label = Integer(i, **kwargs)
            idx += 1
            label.height = label_height
            label.next_to(paragraph[i], DOWN, buff=0)
            labels.add(label)
    return labels

def index_code_labels(
    code: Code,
    label_height: float = 0.1,
    **kwargs,
) -> VGroup:
    ret = VGroup()
    for row in code.code:
        ret.add(index_paragraph_labels(row, label_height, **kwargs))
    return ret
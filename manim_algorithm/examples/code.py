import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from manim import *
from manim_algorithm.code import PythonCode, JavaCode, CppCode

class PyCodeScene(Scene):

    def construct(self):
        code = """
def move_less_or_than_first_item_to_front(a:List[int], l:int, r:int) -> int:
    i = l
    j = r
    x = a[l]
    while i < j:
        while i < j and a[j] > x:
            j -= 1
        while i < j and a[i] <= x:
            i += 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j
"""
        self.play(FadeIn(PythonCode(code=code)))
        self.wait(10)

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": False, "show_in_file_browser": True}):
        scene = PyCodeScene()
        scene.render()
        
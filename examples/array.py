import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manim import *
from manim_algorithm.array import Array
from manim_algorithm.node import Node

class ArrayScene(Scene):

    def construct(self):
        data = [-1, 0, 3, -43.12, ' ', 'abc']
        array1 = Array(data, total_width=10)
        array2 = Array(data, total_width=10, empty_value='/', box_type=Circle, box_color=RED, text_scale=1.5).next_to(array1, DOWN)
        self.play(FadeIn(array1, array2))
        self.wait(1)
        self.play(Node.Select(array1[2]))
        self.wait(1)
        self.play(Node.Unselect(array1[2]))
        self.play(Node.UpdateValue(array1[1], 123))
        node = Node(array1[1].value).next_to(array1, RIGHT)
        self.play(FadeIn(node))
        self.wait(2)

if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True, "show_in_file_browser": True}):
        scene = ArrayScene()
        scene.render()
        
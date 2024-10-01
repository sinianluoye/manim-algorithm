import sys
import os

from manim import *
from ..node import Node


class NodeScene(Scene):

    def construct(self):
        node_list = [Node(1, text_scale=2), Node(1.2, width=3), Node("abc", box_color=RED), Node('a', box_type=Circle), Node(" ")]
        nodes_group = VGroup(*node_list).arrange()
        self.play(FadeIn(nodes_group))
        self.wait(1)
        for i, item in enumerate(node_list):
            self.play(
                Node.Select(
                    item,
                    color=[RED, BLUE, GREEN, YELLOW, PINK][i],
                    opacity=0.8 - i * 0.1,
                ),
                Node.UpdateValue(
                    item,
                    value=[2, -2.13, " ", 'asd', ' '][i],
                )
            )
        for i, item in enumerate(node_list):
            self.play(Node.Unselect(item))
        self.play(FadeOut(nodes_group))

class NodeMoveScene(Scene):

    def construct(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        g1 = VGroup(node1, node2).arrange()
        g2 = VGroup(node3, node4).arrange().next_to(g1, DOWN)
        self.play(FadeIn(g1, g2))
        
        self.play(
            Node.MoveAndOverWrite(node1, node2), 
            Node.MoveAndOverWrite(node3, node4, select_color=RED))
        self.wait(1)


class NodeCopyScene(Scene):

    def construct(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        g1 = VGroup(node1, node2).arrange()
        g2 = VGroup(node3, node4).arrange().next_to(g1, DOWN)
        self.play(FadeIn(g1, g2))
        
        self.play(
            Node.CopyAndOverWrite(node1, node2), 
            Node.CopyAndOverWrite(node3, node4, select_color=RED))
        self.wait(1)

class NodeSwapScene(Scene):

    def construct(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        g1 = VGroup(node1, node2).arrange()
        g2 = VGroup(node3, node4).arrange().next_to(g1, DOWN)
        self.play(FadeIn(g1, g2))
        
        self.play(
            Node.SwapAndOverWrite(node1, node2), 
            Node.SwapAndOverWrite(node3, node4, select_color=RED))
        self.wait(1)
    
class NodeMoveAndOverwriteWithColor(Scene):

    def construct(self):
        node1 = Node(1)
        node2 = Node(2).next_to(node1, RIGHT, buff=1)
        self.play(FadeIn(node1, node2))

        steps = []
        steps.append(Node.Select(node1, color=RED, opacity=0.5))
        
        steps.extend([
            ApplyMethod(node1.move_to, node2),
            AnimationGroup(
                Node.UpdateValue(node2, node1.value), 
                FadeOut(node1)
            )
        ])
        a = Succession(*steps)
        self.play(a, lag_ratio=1, run_time=5)
        print(self.mobjects)
        self.wait(1)

class NodeUpdateValue1(Scene):

    def construct(self):
        node = Node(1)
        self.play(FadeIn(node))
        self.play(Node.UpdateValue(node, 2))
        self.wait(1)

class TestCombine(Scene):

    class CombinedText(VMobject):
        
        def __init__(self):
            super().__init__()
            self.t1 = Text("1")
            self.t2 = Text("2")
            self.add(self.t1, self.t2)
        
        def set_t1_color(self, color):
            self.t1.color = color

    def construct(self):
        obj = self.CombinedText()
        self.play(Succession(*[
            FadeIn(obj),
            obj.animate.set_t1_color(RED),
            FadeOut(obj)
        ]))
        self.wait(1)

if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": False, "save_as_gif": True, "format": "gif"}):
        # scene = NodeUpdateValue1()
        # scene.render()
        
        scene = TestCombine()
        scene.render()
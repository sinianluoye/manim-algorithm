import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from manim import *
from manim_algorithm.node import Node


class NodeScene(Scene):

    def construct(self):
        node_list = [Node(1, text_scale=2), Node(1.2, width=3), Node("abc", box_color=RED), Node(, box_type=Circle), Node(" ")]
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
from typing import List
from .node import Node
from manim import VMobject, Square, RED, Line, LEFT, UP, RIGHT, DOWN, Succession, MoveAlongPath, linear, Point3D, AnimationGroup, FadeOut


class Queue(VMobject):

    def __init__(self, capacity:int, init_data:List[Node]=None,
                 total_width:int=12, font_size:int=48, box_type=Square, bound_color=RED, **kwargs):
        super().__init__(**kwargs)
        self.capacity = capacity
        self.total_width = total_width
        self.item_width = total_width / capacity
        self.font_size = font_size
        self.upbound = Line(LEFT*total_width/2 + UP/2*self.item_width, RIGHT*total_width/2 + UP/2*self.item_width).set_color(bound_color)
        self.downbound = Line(LEFT*total_width/2 + DOWN/2*self.item_width, RIGHT*total_width/2 + DOWN/2*self.item_width).set_color(bound_color)
        self.add(self.upbound, self.downbound)
        self.data:List[Node] = []
        if init_data:
            for item in init_data:
                if not isinstance(item, Node):
                    item = Node(item, width=self.item_width, font_size=font_size, box_type=box_type)
                item.move_to((self.data[-1].get_right() if self.data else self.get_left()) + self.item_width / 2 * RIGHT)
                self.add(item)
                self.data.append(item)


    class Enqueue(Succession):

        def __init__(self, queue:'Queue', item:Node, **kwargs):
            path = [ 
                item.get_center(),
                queue.get_right() + queue.item_width / 2 * RIGHT,
                (queue.data[-1].get_right() if queue.data else queue.get_left()) + queue.item_width / 2 * RIGHT]
            polyline = VMobject()
            polyline.set_points_as_corners(path)
            super().__init__(*[
                MoveAlongPath(item, path=polyline, rate_func=linear, run_time=2),
            ])
            queue.add(item)
            queue.data.append(item)

    class Dequeue(Succession):

        def __init__(self, queue:'Queue', target_pos:Point3D=None, **kwargs):
            if not queue.data:
                return
            item = queue.data[0]
            need_fadout = False
            if target_pos is None:
                target_pos = item.get_center() + DOWN * queue.item_width + LEFT * queue.item_width
                need_fadout = True
            path = [ 
                queue.get_left() + queue.item_width / 2 * LEFT,
                target_pos]
            polyline = VMobject()
            polyline.set_points_as_corners(path)
            animations = [
                AnimationGroup(*[item.animate.shift(LEFT * item.width) for item in queue.data]),
                MoveAlongPath(item, path=polyline, rate_func=linear, run_time=2),
            ]
            if need_fadout:
                animations.append(FadeOut(item))
            super().__init__(*animations)
            queue.remove(item)
            queue.data.pop(0)
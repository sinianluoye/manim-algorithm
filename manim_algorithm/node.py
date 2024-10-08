from typing import Literal, TypeAlias
from manim import *
from manim.typing import ManimFloat, Point3D, Vector3D
from manim.utils.color import ManimColor
from .utils.numpy_helper import NumpyHelper

NodeValue: TypeAlias = str | int | float | None
NodeBoxType: TypeAlias = type[Square] | type[Circle]


class NodeConfig:
    WIDTH = 2
    BOX_TYPE = Square
    BOX_COLOR = WHITE
    SELECT_COLOR = RED
    SELECT_OPACITY = 0.5


class NodeSolt:
    SPLIT_PARTS = 12
    MID = SPLIT_PARTS // 2
    LEFT_MID = (LEFT, MID)
    RIGHT_MID = (RIGHT, MID)
    UP_MID = (UP, MID)
    DOWN_MID = (DOWN, MID)
    LEFT_UP = (LEFT, SPLIT_PARTS // 3 * 2)
    LEFT_DOWN = (LEFT, SPLIT_PARTS // 3)
    RIGHT_UP = (RIGHT, SPLIT_PARTS // 3)
    RIGHT_DOWN = (RIGHT, SPLIT_PARTS // 3 * 2)
    UP_LEFT = (UP, SPLIT_PARTS // 3)
    UP_RIGHT = (UP, SPLIT_PARTS // 3 * 2)
    DOWN_LEFT = (DOWN, SPLIT_PARTS // 3 * 2)
    DOWN_RIGHT = (DOWN, SPLIT_PARTS // 3)
    CORNER_LU = (LEFT, SPLIT_PARTS)
    CORNER_LD = (LEFT, 0)
    CORNER_RU = (RIGHT, 0)
    CORNER_RD = (RIGHT, SPLIT_PARTS)


class Node(VMobject):

    def __init__(
        self,
        value: NodeValue = None,
        width: float = NodeConfig.WIDTH,
        text_scale:float = 1.0,
        box_type: NodeBoxType = NodeConfig.BOX_TYPE,
        box_color: ManimColor = NodeConfig.BOX_COLOR,
        **kwargs,
    ):
        """
        创建一个Node对象, 用于表示一个节点
        Args:
            value (str | int | float | None, optional):
                节点内的值，如果是字符串，展示的时候会以Tex展示. 如果是空串等，会展示为一个半径为0的点作为占位符
                Defaults to None.

            width (int, optional): Node的宽度. Defaults to 2.

            text_scale (float, optional): 文本的缩放比例. Defaults to 1.0.

            box_type (type, optional): Node的形状，Square或Circle. Defaults to Square.

            box_color (ManimColor, optional): Node的颜色. Defaults to WHITE.

        Raises:
            ValueError: _description_
        """

        super().__init__(**kwargs)
        self.set_box(box_type, width, box_color)
        self.text_scale = text_scale
        self.set_value(value)
        self.width = width
    
    def set_box(self, box_type: NodeBoxType, width: float, color: ManimColor) -> 'Node':
        """
        设置节点的形状和颜色

        Args:
            box_type (type): Node的形状，Square或Circle
            width (float): Node的宽度
            color (ManimColor): Node的颜色

        Returns:
            Node: 返回自身
        """
        if hasattr(self, 'box'):
            self.remove(self.box)
        if box_type not in [Square, Circle]:
            raise ValueError("box_type must be Square or Circle")
        if box_type == Square:
            self.box = Square(width)
        elif box_type == Circle:
            self.box = Circle(width / 2)
        self.box.set_color(color)
        self.add(self.box)
        return self

    def get_box(self) -> Mobject:
        return self.box

    def set_value(self, value: NodeValue) -> 'Node':
        if hasattr(self, 'text'):
            self.remove(self.text)
        self.value = value
        if value is None or not str(value).strip():
            self.text = Dot(radius=0)
        else:
            self.text = Tex(str(value)).scale(self.text_scale)
        self.text.move_to(self)
        self.add(self.text)
        return self

    def get_value(self) -> NodeValue:
        return self.value

    def set_fill(self,
        color: ParsableManimColor | None = None,
        opacity: float | None = None,
        family: bool = True,
    ) -> 'Node':
        super().set_fill(color, opacity, False)
        if hasattr(self, 'box'):
            self.box.set_fill(color, opacity, family)
        return self

    def get_fill_color(self) -> ManimColor:
        return self.box.get_fill_color()

    def get_fill_opacity(self) -> ManimFloat:
        return self.box.get_fill_opacity()

    def get_slot(self, direction: Vector3D, index) -> Point3D:
        """
        获取节点的某个方向的插槽, 用于连接指针

        槽位编号:
            槽位方向应为 LEFT RIGHT UP DOWN
            对应方向上的边会被分为12个等分, 顺时针依次编号为0-12, 0和12分别是边的两个端点
            对于圆, 方向所指的边为对应的1/4圆弧

        Args:
            direction (_type_): LEFT or RIGHT or UP or DOWN
            index (_type_): 编号: 0-12
        Returns:
            _type_: 一个点
        """

        proportion = 0
        if NumpyHelper.is_same_direction(direction, RIGHT):
            proportion = 0
        elif NumpyHelper.is_same_direction(direction, LEFT):
            proportion = 0.5
        elif NumpyHelper.is_same_direction(direction, UP):
            proportion = 0.75
        elif NumpyHelper.is_same_direction(direction, DOWN):
            proportion = 0.25
        else:
            raise ValueError("direction must be LEFT or RIGHT or UP or DOWN")
        proportion = proportion + index / NodeSolt.SPLIT_PARTS / 4
        if isinstance(self.box, Square):
            pass
        elif isinstance(self.box, Circle):
            proportion -= 0.125
        else:
            raise ValueError("box_type must be Square or Circle")
        proportion = 1 - proportion
        if proportion > 1:
            proportion -= 1
        if proportion < 0:
            proportion += 1
        return self.box.point_from_proportion(proportion)

    def __str__(self) -> str:
        return f"Node({repr(self.value)})"

    def __repr__(self) -> str:
        return self.__str__()

    class Select(Succession):

        def __init__(
            self,
            *nodes: List["Node"],
            color: ManimColor = NodeConfig.SELECT_COLOR,
            opacity: float = NodeConfig.SELECT_OPACITY,
            **kwargs,
        ):
            """
            选择节点, 用于突出显示
            具体的操作为设置节点的填充颜色

            Args:
                color (ManimColor, optional): 填充的颜色. Defaults to RED.
                opacity (float, optional): 填充颜色的透明度. Defaults to 0.5.
            """
            
            super().__init__(AnimationGroup(*[node.animate.set_fill(color, opacity) for node in nodes]), **kwargs)

    class Unselect(Succession):

        def __init__(self, *nodes: List["Node"], **kwargs):
            """
            取消选择节点, 用于取消突出显示
            具体的操作为设置节点的填充颜色为透明
            """
            super().__init__(AnimationGroup(*[node.animate.set_fill(node.get_fill_color(), 0) for node in nodes]), **kwargs)

    class UpdateValue(Succession):

        def __init__(self, node: "Node", value: NodeValue, **kwargs):
            """
            更新节点的值

            Args:
                value (NodeValue): 新的值
            """
            super().__init__(*[node.animate.set_value(value)], **kwargs)
        
        
    class MoveAndOverWrite(Succession):

        def __init__(self, node: "Node", target: "Node", select_color:ManimColor=None, select_opacity:float=0.2, **kwargs):
            """
            移动并覆盖目标节点

            Args:
                node (Node): 节点
                target (Node): 目标节点
                select_color (ManimColor, optional): 移动过程中是否对正在移动的Node进行选择(染色), None为不染色，非空为染色. Defaults to None.
                select_opacity (float, optional): 染色的透明度. Defaults to 0.2.
            """
            steps = []
            if select_color is not None:
                steps.append(Node.Select(node, color=select_color, opacity=select_opacity))
          
            steps.extend([
                node.animate.move_to(target),
                AnimationGroup(
                    Node.UpdateValue(target, node.value), 
                    FadeOut(node)
                )
            ])
            
            super().__init__(*steps, **kwargs)
        
    class CopyAndOverWrite(Succession):

        def __init__(self, node: "Node", target: "Node", select_color:ManimColor=None, select_opacity:float=0.2, **kwargs):
            """
            复制并覆盖目标节点

            Args:
                node (Node): 节点
                target (Node): 目标节点
                select_color (ManimColor, optional): 移动过程中是否对正在移动的Node进行选择(染色), None为不染色，非空为染色. Defaults to None.
                select_opacity (float, optional): 染色的透明度. Defaults to 0.2.
            """
            copied_node = node.copy().move_to(node)
            steps = [
                FadeIn(copied_node),
                Node.MoveAndOverWrite(copied_node, target, select_color, select_opacity)
            ]
            
            super().__init__(*steps, **kwargs)
    
    class SwapAndOverWrite(Succession):

        def __init__(self, node1: "Node", node2: "Node", select_color:ManimColor=None, select_opacity:float=0.2, **kwargs):
            """
            交换并覆盖目标节点

            Args:
                node1 (Node): 节点1
                node2 (Node): 节点2
                select_color (ManimColor, optional): 移动过程中是否对正在移动的Node进行选择(染色), None为不染色，非空为染色. Defaults to None.
                select_opacity (float, optional): 染色的透明度. Defaults to 0.2.
            """
            copied_node1 = node1.copy().move_to(node1)
            copied_node2 = node2.copy().move_to(node2)
            steps = [
                FadeIn(copied_node1, copied_node2),
            ]
            if select_color is not None:
                steps.append(Node.Select(copied_node1, copied_node2, select_color=select_color, select_opacity=select_opacity))
            steps.append(Swap(copied_node1, copied_node2))
            steps.append(AnimationGroup(
                Node.UpdateValue(node1, copied_node2.value),
                Node.UpdateValue(node2, copied_node1.value),
                FadeOut(copied_node1, copied_node2)
            ))
            super().__init__(*steps, **kwargs)
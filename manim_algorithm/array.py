from .node import *
from typing import List, Iterable, Union

class Array(VMobject):

    def __init__(
        self,
        data:List[NodeValue],
        total_width:float|Node=None,
        box_type=NodeConfig.BOX_TYPE,
        box_color=NodeConfig.BOX_COLOR,
        text_scale:float = 1.0,
        **kwargs
    ):
        """
        创建一个Array对象, 用于表示一个数组

        Args:
            data (List[NodeValue]): 
               数组的内容，注意这里的数组长度是固定的，不支持额外申请空间

            total_width (float, optional):
                数组的总宽度.
            font_size (_type_, optional): 
                数组内元素的字体大小. 
                Defaults to NodeConfig.FONT_SIZE.
            box_type (_type_, optional): 
                数组的box类型.
                Defaults to NodeConfig.BOX_TYPE.
            box_color (_type_, optional): 
                数组box的类型. 
                Defaults to NodeConfig.BOX_COLOR.
            text_scale (float, optional): 
                文本的缩放比例. 
                Defaults to 1.0.
        """
        super().__init__(**kwargs)
        if total_width is None:
            total_width = NodeConfig.WIDTH * len(data)
   
        item_width = total_width / len(data)
        self.array = [
            Node(item, width=item_width, text_scale=text_scale, box_type=box_type, box_color=box_color)
            for item in data
        ]
        self.add(*self.array)
        self.arrange(buff=0)

    @property
    def values(self) -> List[NodeValue]:
        """获取数组内的所有值

        """
        return [item.value for item in self.array]
  

    def __getitem__(self, key: Union[int, slice]) -> Node:
        """获取下标为key的Node 或者 获取切片为key的Arra
        """
        if isinstance(key, slice):
            return Array(self.array[key])
        return self.array[key]

    def __len__(self) -> int:
        return len(self.array)

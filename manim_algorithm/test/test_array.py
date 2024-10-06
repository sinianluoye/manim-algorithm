import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal

import sys
import os
from manim import config as global_config

from ..array import Array
from ..utils.numpy_helper import NumpyHelper
from manim import (
    Square,
    Circle,
    Tex,
    VMobject,
    WHITE,
    RED,
    BLUE,
    GREEN,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    Scene
)
import shutil



class TestArray:

    TEST_MEDIA_DIR = os.path.join(os.path.dirname(__file__), "__test_media_dir__")

    def setup_method(self):
        global_config.media_dir = self.TEST_MEDIA_DIR
        os.makedirs(self.TEST_MEDIA_DIR)

    def teardown_method(self):
        shutil.rmtree(self.TEST_MEDIA_DIR)
        
    """
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
    @pytest.mark.parametrize("data, total_width, box_type, box_color, text_scale", [
        ([1, 2, 3, ' ', 'a'],  10, Square, RED, 1.0),
    ])
    def test_array_initialization(self, data, total_width, box_type, box_color, text_scale):
        array = Array(data, total_width, box_type, box_color, text_scale)
        assert array is not None
        assert len(array.array) == len(data)
        assert array[0].value == data[0]
        assert array[1].value == data[1]
        assert array[2].value == data[2]
        assert array[3].value == data[3]
        assert array[4].value == data[4]
        assert array.values == data
        



if __name__ == "__main__":
    pytest.main()

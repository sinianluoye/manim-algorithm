import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from manim import config as global_config


from manim_algorithm.node import Node, NodeConfig
from manim_algorithm.utils.numpy_helper import NumpyHelper
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


class TestNode:

    TEST_MEDIA_DIR = os.path.join(os.path.dirname(__file__), "__test_media_dir__")

    def setup_method(self):
        global_config.media_dir = self.TEST_MEDIA_DIR
        os.makedirs(self.TEST_MEDIA_DIR)

    def teardown_method(self):
        shutil.rmtree(self.TEST_MEDIA_DIR)

    @pytest.mark.parametrize(
        "value, empty_value, width, box_type, box_color, expected_value, expected_box_type",
        [
            (None, "-", 2, Square, WHITE, "-", Square),
            ("", "-", 2, Square, WHITE, "-", Square),
            ("Hello", "-", 2, Square, WHITE, "Hello", Square),
            (123, "-", 2, Square, WHITE, "123", Square),
            (None, "-", 2, Circle, WHITE, "-", Circle),
            ("", "-", 2, Circle, WHITE, "-", Circle),
            ("Hello", "-", 2, Circle, WHITE, "Hello", Circle),
            (123, "-", 2, Circle, WHITE, "123", Circle),
        ],
    )
    def test_node_initialization(
        self,
        value,
        empty_value,
        width,
        box_type,
        box_color,
        expected_value,
        expected_box_type,
    ):
        node = Node(
            value=value,
            empty_value=empty_value,
            width=width,
            box_type=box_type,
            box_color=box_color,
        )

        assert node.value == value
        assert node.text.tex_string == str(expected_value)
        assert isinstance(node.box, expected_box_type)
        if box_type == Square:
            assert node.box.width == width
        else:
            assert node.box.radius == width / 2

    @pytest.mark.parametrize(
        "direction, index, box_type, expected",
        [
            (RIGHT, 0, Square, np.array((1, 1, 0))),
            (RIGHT, 6, Square, np.array((1, 0, 0))),
            (LEFT, 0, Square, np.array((-1, -1, 0))),
            (UP, 0, Square, np.array((-1, 1, 0))),
            (DOWN, 0, Square, np.array((1, -1, 0))),
            (RIGHT, 7, Square, np.array((1, -1 / 6, 0))),
            (
                RIGHT,
                7,
                Circle,
                np.array((np.cos(-np.pi / 24), np.sin(-np.pi / 24), 0)),
            ),  # 圆形对应的角度为 2*pi/48
        ],
    )
    def test_node_get_slot(self, direction, index, box_type, expected):
        node = Node(box_type=box_type, width=2)
        point = node.get_slot(direction, index)
        # 由于manim的圆形计算point_from_proportion是通过曲线计算的，所以存在一定的误差
        # 这里atol=1e-3
        assert NumpyHelper.is_equal_vector(
            point, expected, atol=1e-3
        ), f"{point} != {expected}"


if __name__ == "__main__":
    pytest.main()

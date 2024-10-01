import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from manim_algorithm.utils.numpy_helper import NumpyHelper


class TestNumpyHelper:

    @pytest.mark.parametrize(
        "v, expected",
        [
            (np.array([3.0, 4.0]), np.array([0.6, 0.8])),
            (np.array([0.0, 0.0]), np.array([0.0, 0.0])),
            (np.array([1.0, 0.0]), np.array([1.0, 0.0])),
            (np.array([-3.0, -4.0]), np.array([-0.6, -0.8])),
            (
                np.array([1.0, 2.0, 2.0]),
                np.array([1.0, 2.0, 2.0]) / np.linalg.norm([1.0, 2.0, 2.0]),
            ),
        ],
    )
    def test_normalize_vector(self, v, expected):
        result = NumpyHelper.normalize_vector(v)
        assert_array_almost_equal(result, expected)

    @pytest.mark.parametrize(
        "v1, v2, expected",
        [
            (np.array([1.0, 2.0]), np.array([1.0, 2.0]), True),
            (np.array([1.0, 2.0]), np.array([1.0, 2.1]), False),
            (np.array([1.0, 2.0]), np.array([-1.0, -2.0]), False),
            (np.array([1.0, 2.0]), np.array([1.0, 2.0, 3.0]), "ValueError"),
        ],
    )
    def test_is_equal_vector(self, v1, v2, expected):
        if expected == "ValueError":
            with pytest.raises(ValueError):
                NumpyHelper.is_equal_vector(v1, v2)
        else:
            result = NumpyHelper.is_equal_vector(v1, v2)
            assert np.all(result) == expected

    @pytest.mark.parametrize(
        "v1, v2, expected",
        [
            (np.array([3.0, 4.0]), np.array([6.0, 8.0]), True),
            (np.array([3.0, 4.0]), np.array([6.0, 7.0]), False),
            (np.array([3.0, 4.0]), np.array([-3.0, -4.0]), False),
            (np.array([0.0, 0.0]), np.array([1.0, 1.0]), False),
            (np.array([1.0, 2.0, 2.0]), np.array([2.0, 4.0, 4.0]), True),
        ],
    )
    def test_is_same_direction(self, v1, v2, expected):
        result = NumpyHelper.is_same_direction(v1, v2)
        assert result == expected


if __name__ == "__main__":
    pytest.main()

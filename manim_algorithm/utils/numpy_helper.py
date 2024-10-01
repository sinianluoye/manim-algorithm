import numpy as np
from numpy.typing import NDArray


class NumpyHelper:

    @staticmethod
    def normalize_vector(v: NDArray):
        """
        将向量 v 归一化为单位向量
        :param v: 输入向量（numpy 数组）
        :return: 单位向量（numpy 数组）
        """
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    @staticmethod
    def is_equal_vector(
        v1: NDArray, v2: NDArray, rtol: float = 1e-5, atol: float = 1e-8
    ):
        return np.isclose(v1, v2, rtol=rtol, atol=atol).all()

    @staticmethod
    def is_same_direction(
        v1: NDArray, v2: NDArray, rtol: float = 1e-5, atol: float = 1e-8
    ):
        return NumpyHelper.is_equal_vector(
            NumpyHelper.normalize_vector(v1),
            NumpyHelper.normalize_vector(v2),
            rtol=rtol,
            atol=atol,
        )

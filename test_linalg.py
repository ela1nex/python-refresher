import linear_algebra
import unittest
import numpy as np
import math


a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])

a2 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])

a4 = np.array([[1, 2, 3], [4, 5, 6]])
b4 = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

a5 = np.array([1, 1, 2])


class TestLinAlg(unittest.TestCase):
    def test_add(self):
        self.assertEqual(
            np.array([5, 7, 9]).all(),
            linear_algebra.matrix_sum(a1, b1).all(),
        )
        self.assertEqual(
            np.array([[6, 8], [10, 12]]).all(),
            linear_algebra.matrix_sum(a2, b2).all(),
        )

    def test_difference(self):
        self.assertEqual(
            np.array([-3, -3, -3]).all(),
            linear_algebra.matrix_difference(a1, b1).all(),
        )
        self.assertEqual(
            np.array([[-4, -4], [-4, -4]]).all(),
            linear_algebra.matrix_difference(a2, b2).all(),
        )

    def test_dp(self):
        self.assertEqual(32, linear_algebra.dot_product(a1, b1))

    def test_product(self):
        self.assertEqual(
            np.array([[74, 80, 86, 92], [173, 188, 203, 218]]).all(),
            linear_algebra.product(a4, b4).all(),
        )

    def test_magnitude(self):
        self.assertEqual(math.sqrt(6), linear_algebra.magnitude(a5))

    def test_transposition(self):
        self.assertEqual(
            np.array([[1, 3], [2, 4]]).all(), linear_algebra.transpose(a2).all()
        )


if __name__ == "__main__":
    unittest.main()

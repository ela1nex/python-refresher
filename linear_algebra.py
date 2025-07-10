import numpy as np


def matrix_sum(a, b):
    """Returns the sum of matrices a and b."""
    if type(a) == np.ndarray and type(b) == np.ndarray:
        return np.add(a, b)


def matrix_difference(a, b):
    """Returns the difference of matrices a and b."""
    if type(a) == np.ndarray and type(b) == np.ndarray:
        return np.subtract(a, b)


def dot_product(a, b):
    """Returns the dot product of matrices a and b"""
    if type(a) == np.ndarray and type(b) == np.ndarray:
        return np.dot(a, b)


def product(a, b):
    """Returns the product of matrices a and b."""
    if type(a) == np.ndarray and type(b) == np.ndarray:
        return np.matmul(a, b)


def magnitude(a):
    """Returns the magnitude of matrix a."""
    if type(a) == np.ndarray:
        return np.linalg.norm(a)


def transpose(a):
    """Returns the transposition of matrix a."""
    if type(a) == np.ndarray:
        return np.transpose(a)

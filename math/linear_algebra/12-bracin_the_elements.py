#!/usr/bin/env python3
"""Module that performs element-wise operations on two matrices."""


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, subtraction,
    multiplication, and division on mat1 and mat2."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

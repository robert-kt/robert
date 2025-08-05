import os
import sys

import pytest

# Ensure the repository root is on the module search path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import calculate


@pytest.mark.parametrize(
    "a, b, op, expected",
    [
        (2, 3, '+', 5),
        (5, 2, '-', 3),
        (3, 4, '*', 12),
        (10, 2, '/', 5),
    ],
)
def test_calculate(a, b, op, expected):
    assert calculate(a, b, op) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculate(1, 0, '/')


def test_unsupported_operation():
    with pytest.raises(ValueError):
        calculate(1, 1, '^')

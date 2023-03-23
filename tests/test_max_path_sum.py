import pytest

from solutions.max_path_sum import Triangle


@pytest.fixture
def small_triangle():
    return [[0],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4],
            [1, 2, 3, 4, 5]]


@pytest.fixture
def small_triangle_expected():
    return [[0],
            [1, 2],
            [2, 4, 5],
            [3, 6, 8, 9],
            [4, 8, 11, 13, 14]]


@pytest.fixture
def small_triangle_expected_choices():
    return [0, 2, 3, 4, 5]


def test_triangle_setup(small_triangle):
    triangle = Triangle(small_triangle)
    assert triangle.triangle_numbers == small_triangle


def test_triangle_calculate_totals(small_triangle, small_triangle_expected):
    triangle = Triangle(small_triangle)
    triangle.calculate_totals()
    assert triangle.triangle_totals == small_triangle_expected


def test_triangle_final_score(small_triangle):
    triangle = Triangle(small_triangle)
    triangle.calculate_totals()
    assert triangle.final_score() == 14

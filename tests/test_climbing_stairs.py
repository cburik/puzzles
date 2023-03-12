from solutions.climbing_stairs import permutation_calculator
from solutions.climbing_stairs import faster_permutation_calculator


def test_one():
    assert permutation_calculator(1, 2) == 1


def test_two_two():
    assert permutation_calculator(2, 2) == 2


def test_four_two():
    assert permutation_calculator(4, 2) == 5


def test_three_three():
    assert permutation_calculator(3, 3) == 4


def test_very_large_step():
    assert permutation_calculator(2, 10) == 2


def test_one_f():
    assert faster_permutation_calculator(1, 2) == 1


def test_two_two_f():
    assert faster_permutation_calculator(2, 2) == 2


def test_four_two_f():
    assert faster_permutation_calculator(4, 2) == 5


def test_three_three_f():
    assert faster_permutation_calculator(3, 3) == 4


def test_very_large_step_f():
    assert faster_permutation_calculator(2, 10) == 2
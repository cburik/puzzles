import pytest
from solutions.tower_of_hanoi.main import solve_tower
from solutions.tower_of_hanoi.model import Tower


@pytest.fixture
def expected_state_n3():
    initial_list = list(range(3))
    initial_list.reverse()
    return {'A': [], 'B': [], 'C': initial_list}


@pytest.fixture
def expected_state_n10():
    initial_list = list(range(10))
    initial_list.reverse()
    return {'A': [], 'B': [], 'C': initial_list}


def test_n1():
    solution = solve_tower(1)
    assert solution == [['A', 'C']]


def test_n3(expected_state_n3):
    solution = solve_tower(3)
    tower = Tower(3)
    for move in solution:
        print(move)
        tower.move(move[0], move[1])
    assert tower.state == expected_state_n3


def test_n10(expected_state_n10):
    solution = solve_tower(10)
    tower = Tower(10)
    for move in solution:
        tower.move(move[0], move[1])
    assert tower.state == expected_state_n10

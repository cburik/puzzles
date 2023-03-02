from typing import List


def solve_tower(n: int, labels: List[str] = ['A', 'B', 'C']) -> list:
    """Solves the tower of Hanoi. Returns list of moves"""
    if n == 1:
        return [[labels[0], labels[2]]]

    moves = solve_tower(n-1, [labels[0], labels[2], labels[1]])
    moves.append([labels[0], labels[2]])
    moves += solve_tower(n-1, [labels[1], labels[0], labels[2]])
    return moves


def pprint_moves(moves: List[List[str]]):
    output = 'Solution, move top disc from x to x:'
    for move in moves:
        output += f'\n{move[0]} to {move[1]}'
    print(output)


if __name__ == '__main__':
    pprint_moves(solve_tower(3))

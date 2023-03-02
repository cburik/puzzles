from typing import List


class Tower(object):
    def __init__(self, n: int, labels: List[str] = ['A', 'B', 'C']):
        if len(labels) != 3:
            raise ValueError("Unexpected number of labels")
        initial_list = list(range(n))
        initial_list.reverse()
        self.state: dict = {labels[0]: initial_list, labels[1]: [], labels[2]: []}
        self.move_history = []

    def _valid_move(self, start: str, end: str) -> bool:
        """checks if it's a valid move"""
        if start not in self.state.keys() or end not in self.state.keys():
            return False
        if self.state[start] == []:
            return False
        if self.state[end] == []:
            return True
        return self.state[start][-1] < self.state[end][-1]

    def move(self, start: str, end: str):
        if self._valid_move(start, end):
            disc = self.state[start].pop()
            self.state[end].append(disc)
        else:
            raise ValueError('Invalid Move')

        self.move_history.append([start, end])

from typing import List, Optional


class Triangle(object):
    def __init__(self, triangle_numbers: List[List[int]]):
        self.triangle_numbers: List[List[int]] = triangle_numbers
        self.triangle_totals: Optional[List[List[int]]] = None

    def calculate_totals(self):
        i = 0
        self.triangle_totals = []
        self.triangle_totals.append(self.triangle_numbers[0])
        for i in range(1, len(self.triangle_numbers)):
            row = self.triangle_numbers[i]
            row_totals = row.copy()
            row_totals[0] += self.triangle_totals[i - 1][0]
            row_totals[-1] += self.triangle_totals[i - 1][-1]
            for j in range(1, len(row) - 1):
                row_totals[j] += max(self.triangle_totals[i - 1][j - 1], self.triangle_totals[i - 1][j])

            self.triangle_totals.append(row_totals)

    def final_score(self):
        return max(self.triangle_totals[-1])


if __name__ == "__main__":
    from timeit import timeit

    input_triangle = []
    with open("other/triangle.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(" ")
            row = []
            for el in line:
                el = el.strip()
                row.append(int(el))
            input_triangle.append(row)

    triangle = Triangle(input_triangle)
    print(timeit(triangle.calculate_totals, number=1000) / 1000)
    print(triangle.final_score())

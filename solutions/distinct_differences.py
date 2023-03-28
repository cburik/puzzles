"""
Solution to the distinct differences problem.

Given an array A[] of length N. For each index, i (1<=i<=N), find the difference between the number of
distinct elements in it's left and right side in the array.

Example 1:

Input:
N = 3
arr[] = {4, 3, 3}
Output: {-1, 0, 2}

Explanation: For index i=1, there are 0 distinct element in the left side of it,
and 1 distinct element(3) in it's right side. So difference is 0-1 = -1.
Similarly for index i=2, there is 1 distinct element (4) in left side of it,
and 1 distinct element(3) in it's right side. So difference is 1-1 = 0.
Similarly for index i=3, there are 2 distinct elements (4 and 3) in left side of it,
and 0 distinct elements in it's left side. So difference is 2-0 = 2.
"""
from typing import List, Tuple


def get_number_of_distinct_elements(input_list: list) -> int:
    """Returns the number of distinct elements in a list"""
    return len(set(input_list))


def split_list_on_index(input_list: list, index: int) -> Tuple[list, list]:
    """Splits a list on a index and returns two lists"""
    left_list = input_list[:index]
    right_list = input_list[index + 1 :]
    return (left_list, right_list)


def get_distinct_difference(input_list: List[int]) -> List[int]:
    """Main"""
    distinct_difference = []
    for i in range(0, len(input_list)):
        left_list, right_list = split_list_on_index(input_list, i)
        n_distinct_left = get_number_of_distinct_elements(left_list)
        n_distinct_right = get_number_of_distinct_elements(right_list)
        difference = n_distinct_left - n_distinct_right
        distinct_difference.append(difference)

    return distinct_difference


if __name__ == '__main__':
    get_distinct_difference([4, 4, 3, 3])

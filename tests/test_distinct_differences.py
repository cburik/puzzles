from solutions.distinct_differences import get_distinct_difference, get_number_of_distinct_elements, split_list_on_index


def test_split_list_on_index():
    assert split_list_on_index([4, 3, 3], 1) == ([4], [3])


def test_get_number_of_distinct_elements():
    assert get_number_of_distinct_elements([4, 3, 3]) == 2


def test_get_number_of_distinct_elements_empty():
    assert get_number_of_distinct_elements([]) == 0


def test_get_distinct_difference1():
    assert get_distinct_difference([4, 3, 3]) == [-1, 0, 2]


def test_get_distinct_difference2():
    assert get_distinct_difference([4, 4, 3, 3]) == [-2, 0, 0, 2]

from solutions.hamming_distance import (count_str_differences, hamming_distance, int_to_32bit_binary_str,
                                        total_hamming_distance)


def test_int_to_32bit_binary_str_0():
    assert int_to_32bit_binary_str(0) == 32 * "0"


def test_int_to_32bit_binary_str_1():
    assert int_to_32bit_binary_str(1) == 31 * "0" + "1"


def test_int_to_32bit_binary_str_4():
    assert int_to_32bit_binary_str(4) == 29 * "0" + "100"


def test_count_str_differences_no_diff():
    assert count_str_differences("hello", "hello") == 0


def test_count_str_differences_diff():
    assert count_str_differences("hezzo", "hello") == 2


def test_hamming_distance():
    assert hamming_distance(4, 1) == 2


def test_total_hamming_distance_2_elements():
    assert total_hamming_distance([4, 1]) == 2


def test_total_hamming_distance_3_elements():
    assert total_hamming_distance([4, 14, 4]) == 4

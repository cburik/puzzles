"""Solution to calculate the hamming distance problem"""
from typing import List


def int_to_32bit_binary_str(integer: int) -> str:
    """Converts an integer to 32 bit binary string"""
    return format(integer, '032b')


def count_str_differences(string_a: str, string_b: str) -> int:
    """Counts the differences in string characters for equal length strings"""
    differences = 0
    for char_a, char_b in zip(string_a, string_b):
        differences += 1 if char_a != char_b else 0
    return differences


def hamming_distance(int_x: int, int_y: int) -> int:
    """Returns the hamming distance of two integers"""
    x_formatted = int_to_32bit_binary_str(int_x)
    y_formatted = int_to_32bit_binary_str(int_y)
    return count_str_differences(x_formatted, y_formatted)


def total_hamming_distance(integers: List[int]) -> int:
    """Calculates the total hamming distance between all integers in a list"""
    count = 0
    while len(integers) > 1:
        integer = integers.pop()
        for i in integers:
            count += hamming_distance(integer, i)
    return count

def count_string(string: str) -> dict:
    counts = {}
    for char in set(string):
        counts[char] = string.count(char)
    return counts

def anagram_checker(string_one: str, string_two: str) -> bool:    
    counts_one = count_string(string_one)
    counts_two = count_string(string_two)
    return counts_one == counts_two

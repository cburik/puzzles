"""Solves puzzle for the anagram checker"""


def count_string(input_str: str) -> dict:
    """Counts number of each symbols in a dict"""
    counts = {}
    for char in set(input_str):
        counts[char] = input_str.count(char)
    return counts


def anagram_checker(string_one: str, string_two: str) -> bool:
    """Checks if a string is are an anagram of eachother"""
    counts_one = count_string(string_one)
    counts_two = count_string(string_two)
    return counts_one == counts_two


if __name__ == '__main__':
    import random
    import string

    import big_o

    def other_anagram(string_list):
        """helper"""
        return anagram_checker(string_list[0], string_list[1])

    best, others = big_o.big_o(
        other_anagram,
        lambda n: [
            ''.join(
                random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k=n,
                )
            ),
            ''.join(
                random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k=n,
                )
            ),
        ],
        n_repeats=3000,
    )

    print(best)
    # for class_, residuals in others.items():
    #     print('{!s:<60s}    (res: {:.2G})'.format(class_, residuals))

from solutions.anagram_checker import anagram_checker


def test_hello():
    assert anagram_checker('hello', 'olleh')


def test_capital():
    assert not anagram_checker('ha!', 'H!a')


def test_fail():
    assert not anagram_checker('hello', 'helo')


def test_empty():
    assert not anagram_checker('ah', '')


def test_both_empty():
    assert anagram_checker('', '')

"""Return longest word in list of words.

For example::

    >>> find_longest_word(["hi", "hello"])
    5

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12

"""


def find_longest_word(words):
    """Return longest word in list of words."""

    max_word = len(words[0])

    for word in words:
    	if len(word) > max_word:
    		max_word = len(word)
    return max_word


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE MAX!\n")

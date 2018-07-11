"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    nums_dict = {}

    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    highest = max(nums_dict.values())
    mode = set()
    for num, count in nums_dict.items():
        if count == highest:
            mode.add(num)
    return mode

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")

"""Write a function that takes a list of characters and reverses the letters in-place.

For example:

        >>> reverse_list_in_place([])
        []

        >>> reverse_list_in_place(['a', 'b', 'c', 'd'])
        ['d', 'c', 'b', 'a']

"""


def reverse_list_in_place(lst):
    left_index = 0
    right_index = len(lst) - 1

    while left_index < right_index:
        lst[left_index], lst[right_index] = lst[right_index], lst[left_index]
        left_index += 1
        right_index -= 1
    return lst
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"

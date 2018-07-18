"""Given an array, find the item's index. If not found, return None.

	>>> find_item([1, 2, 3, 4, 5], 6)
	

	>>> find_item([10, 13, 20, -2, -33], -33)
	4


"""


def find_item(array, item):
	"""Given an array, find the item"""
	for i in range(len(array)):
		if array[i] == item:
			return i
	return None


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
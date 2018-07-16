"""Use selection sort to sort the array

	>>> selection_sort([5, 4, 3, 2, 1])
	[1, 2, 3, 4, 5]

	>>> selection_sort([4, 5, 3, 2, -1])
	[-1, 2, 3, 4, 5]

	>>> selection_sort([-1, -2, -3, -4, -5])
	[-5, -4, -3, -2, -1]

"""

def selection_sort(array):
	"""Using selection sort, return the sorted array"""

	for i in range(len(array)-1, 0, -1):
		max_value = 0
		for j in range(1, i + 1):
			if array[j] > array[max_value]:
				max_value = j
		if i != max_value:
			temp = array[i]
			array[i] = array[max_value]
			array[max_value] = temp

	return array


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")
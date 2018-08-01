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

	for i in range(0,len(array) - 1):
		min_value = i
		for j in range(i + 1, len(array)):
			if array[j] < array[min_value]:
				min_value = j
		if min_value != i:
			array[i], array[min_value] = array[min_value], array[i]

	return array


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")
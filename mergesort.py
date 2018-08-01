"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""

    # if lst < 2:
    # 	return lst
    if len(lst) > 1:
	    mid = len(lst) // 2
	    left = lst[mid:]
	    right = lst[:mid]

	    merge_sort(left)
	    merge_sort(right)

	    left_ind = right_ind = new_ind = 0

	    while left_ind < len(left) and right_ind < len(right):
	    	if left[left_ind] < right[right_ind]:
	    		lst[new_ind] = left[left_ind]
	    		left_ind += 1

	    	else:
	    		lst[new_ind] = right[right_ind]
	    		right_ind += 1
	    	new_ind += 1
	    
	    while left_ind < len(left):
	    	lst[new_ind] = left[left_ind]
	    	left_ind += 1
	    	new_ind += 1

	    while right_ind < len(right):
	    	lst[new_ind] = right[right_ind]
	    	right_ind += 1
	    	new_ind += 1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")

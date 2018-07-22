"""There are a bunch of numbers in an array. One of these numbers occurs once in the array. Other numbers occur at least twice.
Write a function that returns the lonely integer.

>>> find_lonely_num([2, 6, 3, 8, 3, 2, 6])
8

"""

def find_lonely_num(nums):
	nums_dict = {}

	for num in nums:
		count = nums_dict.get(num, 0)
		nums_dict[num] = count + 1

	for value, count in nums_dict.iteritems():
		if count == 1:
			return value



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")
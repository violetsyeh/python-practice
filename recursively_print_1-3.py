"""Rescursively print the numbers 1 to 3.

>>> count()
1
2
3

"""

def count(n=1):
	"""Use recursion to print 1 - 3"""

	if n > 3:
		return
	print n
	count(n + 1)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")
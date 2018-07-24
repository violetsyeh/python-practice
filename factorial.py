"""Write a program that takes in a number, n, and outputs n!

>>> factorial(1)
1

>>> factorial(4)
24

"""

def factorial(n):
	"""Return factorial of n."""
	
	result = 1
	
	while n != 0:
		result *= n
		n -= 1
	return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
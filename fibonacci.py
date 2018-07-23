"""Use recursion to solve Fibonacci.

>>> fib_recursive(1)
1

>>> fib_recursive(5)
5

>>> fib_recursive(8)
21

>>> fib_recursive(10)
55

"""

def fib_recursive(n):

	if n <= 1:
		return n
	return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
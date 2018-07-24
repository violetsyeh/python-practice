"""Write the function reverse that takes one string as an argument 
and returns that string in reverse. Do not use any built-in methods.

>>> reverse_string('I love you')
'uoy evol I'

"""

def reverse_string(str):
	"""Return string reversed."""

	rev_str = ''

	for num in range(len(str) - 1, -1, -1):
		rev_str += str[num]
	return rev_str

	# return ''.join(reversed(str))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"

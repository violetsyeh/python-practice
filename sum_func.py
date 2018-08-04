"""
Problem 2
Given an integer, create a function which returns the sum of all the 
individual digits in that integer. For example: if n = 4321, return 4+3+2+1

>>> sum_func(4321)
10


>>> sum_func(0)
0

>>> sum_func(1010)
2

"""


def sum_func(n):

    if n == 0:
        return 0
    
    else:
        return (n % 10) + sum_func(int(n / 10))




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
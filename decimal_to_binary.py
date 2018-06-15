"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'
"""

def dec2bin(num):
    """Convert a decimal number to binary representation."""
    num_to_bin = ''

    if num == 0:
        num_to_bin += str(num)
    else:
        while num > 0:
            bin_digit = num % 2
            num_to_bin = str(bin_digit) + num_to_bin
            num = num / 2
    return num_to_bin

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
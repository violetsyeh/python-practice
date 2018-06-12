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

print dec2bin(6)
print dec2bin(0)
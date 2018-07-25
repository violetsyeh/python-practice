import unittest

def is_unique(str):
	"""Write a function that checks if a string has all unique characters"""

	#Assuming character set is ASCII
	if len(str) > 128:
		return False

	char_set = [False for _ in range(128)]

	for char in str:
		val = ord(char)
		if char_set[val] == True:
			return False
		char_set[val] = True
	return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
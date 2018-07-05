import unittest


def has_palindrome_permutation(the_string):

	# Check if any permutation of the input is a palindrome

	Setchecker = set()

	for i in the_string:
		if i in Setchecker:
			Setchecker.remove(i)
		else:
			Setchecker.add(i)
	

	return len(Setchecker)<=1


















# Tests

class Test(unittest.TestCase):

	def test_permutation_with_odd_number_of_chars(self):
		result = has_palindrome_permutation('aabcbcd')
		self.assertTrue(result)

	def test_permutation_with_even_number_of_chars(self):
		result = has_palindrome_permutation('aabccbdd')
		self.assertTrue(result)

	def test_no_permutation_with_odd_number_of_chars(self):
		result = has_palindrome_permutation('aabcd')
		self.assertFalse(result)

	def test_no_permutation_with_even_number_of_chars(self):
		result = has_palindrome_permutation('aabbcd')
		self.assertFalse(result)

	def test_empty_string(self):
		result = has_palindrome_permutation('')
		self.assertTrue(result)

	def test_one_character_string(self):
		result = has_palindrome_permutation('a')
		self.assertTrue(result)


unittest.main(verbosity=2)
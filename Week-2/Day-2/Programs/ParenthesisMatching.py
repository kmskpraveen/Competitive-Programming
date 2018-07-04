import unittest


def get_closing_paren(sentence, opening_paren_index):

	# Find the position of the matching closing parenthesis
	
	opener = 0
	count = 0

	if (opening_paren_index+1<=len(sentence)-1):
		for i in range(opening_paren_index+1,len(sentence)):
			if sentence[i] == '(':
				opener = opener+1
			else:
				opener = opener-1
			count = count+1
			if opener < 0:
				return opening_paren_index+count

	raise Exception


















# Tests

class Test(unittest.TestCase):

	def test_all_openers_then_closers(self):
		actual = get_closing_paren('((((()))))', 2)
		expected = 7
		self.assertEqual(actual, expected)


	def test_mixed_openers_and_closers(self):
		actual = get_closing_paren('()()((()()))', 5)
		expected = 10
		self.assertEqual(actual, expected)

	def test_no_matching_closer(self):
		with self.assertRaises(Exception):
			get_closing_paren('()(()', 2)


unittest.main(verbosity=2)
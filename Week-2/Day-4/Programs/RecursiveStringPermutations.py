import unittest


def get_permutations(string):

	# Generate all permutations of the input string
	if(len(string)==0):
		return set([''])
	if (len(string) == 1):
		return set(string)

	first_char = string[0]
	all_except_first = string[1:]
	permutations_all_except_first = get_permutations(all_except_first)

	permutations = set()

	for word in permutations_all_except_first:
		for position in range(len(all_except_first) + 1):
			permutations.add(word[:position] + first_char + word[position:])

	# print(permutations)
	return permutations
















# Tests

class Test(unittest.TestCase):

	def test_empty_string(self):
		actual = get_permutations('')
		expected = set([''])
		self.assertEqual(actual, expected)

	def test_one_character_string(self):
		actual = get_permutations('a')
		expected = set(['a'])
		self.assertEqual(actual, expected)

	def test_two_character_string(self):
		actual = get_permutations('ab')
		expected = set(['ab', 'ba'])
		self.assertEqual(actual, expected)

	def test_three_character_string(self):
		actual = get_permutations('abc')
		expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)
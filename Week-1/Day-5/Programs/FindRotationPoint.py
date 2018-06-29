import unittest


def find_rotation_point(words):

	# Find the rotation point in the list	
	minimum = 0
	maximum = len(words) - 1
	firstWord = words[0]

	while minimum < maximum:
		check = (minimum + maximum) // 2
		
		if words[check] < firstWord:
			maximum = check	
		else:
			minimum = check
		
		if minimum + 1 == maximum :
			break
	
	return maximum


















# Tests

class Test(unittest.TestCase):

	def test_small_list(self):
		actual = find_rotation_point(['cape', 'cake'])
		expected = 1
		self.assertEqual(actual, expected)

	def test_medium_list(self):
		actual = find_rotation_point(['grape', 'orange', 'plum',
											  'radish', 'apple'])
		expected = 4
		self.assertEqual(actual, expected)

	def test_large_list(self):
		actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
											  'undulate', 'xenoepist', 'asymptote',
											  'babka', 'banoffee', 'engender',
											  'karpatka', 'othellolagkage'])
		expected = 5
		self.assertEqual(actual, expected)

	 # Are we missing any edge cases?


unittest.main(verbosity=2)
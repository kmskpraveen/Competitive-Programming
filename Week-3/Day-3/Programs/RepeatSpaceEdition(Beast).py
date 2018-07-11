import unittest


def find_repeat(the_list):

	# Find a number that appears more than once
	length = len(the_list)
	slow = length
	fast = length

	while(True):
		slow = the_list[slow-1]
		fast = the_list[fast-1]
		fast = the_list[fast-1]

		if slow==fast:
			break

	fast = length

	while(True):
		slow = the_list[slow-1]
		fast = the_list[fast-1]

		if slow==fast:
			return slow



















# Tests

class Test(unittest.TestCase):

	def test_just_the_repeated_number(self):
		actual = find_repeat([1, 1])
		expected = 1
		self.assertEqual(actual, expected)

	def test_short_list(self):
		actual = find_repeat([1, 2, 3, 2])
		expected = 2
		self.assertEqual(actual, expected)

	def test_medium_list(self):
		actual = find_repeat([1, 2, 5, 5, 5, 5])
		expected = 5
		self.assertEqual(actual, expected)

	def test_long_list(self):
		actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
		expected = 4
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)
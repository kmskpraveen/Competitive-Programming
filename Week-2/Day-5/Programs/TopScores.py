import unittest


def sort_scores(unsorted_scores, highest_possible_score):

	# Sort the scores in O(n) time

	ListCount = [0 for i in range(highest_possible_score+1)]

	for i in unsorted_scores:
		ListCount[i] += 1

	k = 0
	for i in range(highest_possible_score,-1,-1):
		for j in range(ListCount[i]):
			unsorted_scores[k] = i
			k += 1

	return unsorted_scores


















# Tests

class Test(unittest.TestCase):

	def test_no_scores(self):
		actual = sort_scores([], 100)
		expected = []
		self.assertEqual(actual, expected)

	def test_one_score(self):
		actual = sort_scores([55], 100)
		expected = [55]
		self.assertEqual(actual, expected)

	def test_two_scores(self):
		actual = sort_scores([30, 60], 100)
		expected = [60, 30]
		self.assertEqual(actual, expected)

	def test_many_scores(self):
		actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
		expected = [91, 89, 65, 53, 41, 37]
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)
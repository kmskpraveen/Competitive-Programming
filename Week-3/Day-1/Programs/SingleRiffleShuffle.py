import unittest


def is_single_riffle(half1, half2, shuffled_deck):

	# Check if the shuffled deck is a single riffle of the halves



	l1 = 0
	l2 = 0
	trigger = 0
	for i in shuffled_deck:
		if l1<len(half1) and half1[l1] == i:
			l1 = l1 + 1
			trigger = 1
		if l2<len(half2) and half2[l2] == i:
			l2 = l2 + 1
			trigger = 2
		if (trigger == 1 or trigger == 2):
			trigger = 0
		else:
			return False

	return True


















# Tests

class Test(unittest.TestCase):

	def test_both_halves_are_the_same_length(self):
		result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
		self.assertTrue(result)

	def test_halves_are_different_lengths(self):
		result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
		self.assertFalse(result)

	def test_one_half_is_empty(self):
		result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
		self.assertTrue(result)

	def test_shuffled_deck_is_missing_cards(self):
		result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
		self.assertFalse(result)

	def test_shuffled_deck_has_extra_cards(self):
		result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
		self.assertFalse(result)


unittest.main(verbosity=2)
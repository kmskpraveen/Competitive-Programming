import unittest


def merge_lists(my_list, alices_list):

	# Combine the sorted lists into one large sorted list
	sorted_array = []
	i1 = 0
	i2 = 0

	while(True):
		if(len(sorted_array)==len(my_list)+len(alices_list)):
			break
		if i1==len(my_list):
			for i in alices_list[i2:]:
				sorted_array.append(i)
		elif i2==len(alices_list):
			for i in my_list[i1:]:
				sorted_array.append(i)
		else:
			if(my_list[i1]<=alices_list[i2]):
				sorted_array.append(my_list[i1])
				i1 = i1+1
			else:
				sorted_array.append(alices_list[i2])
				i2 = i2+1
		# print(sorted_array)
	return sorted_array


















# Tests

class Test(unittest.TestCase):

	def test_both_lists_are_empty(self):
		actual = merge_lists([], [])
		expected = []
		self.assertEqual(actual, expected)

	def test_first_list_is_empty(self):
		actual = merge_lists([], [1, 2, 3])
		expected = [1, 2, 3]
		self.assertEqual(actual, expected)

	def test_second_list_is_empty(self):
		actual = merge_lists([5, 6, 7], [])
		expected = [5, 6, 7]
		self.assertEqual(actual, expected)

	def test_both_lists_have_some_numbers(self):
		actual = merge_lists([2, 4, 6], [1, 3, 7])
		expected = [1, 2, 3, 4, 6, 7]
		self.assertEqual(actual, expected)

	def test_lists_are_different_lengths(self):
		actual = merge_lists([2, 4, 6, 8], [1, 7])
		expected = [1, 2, 4, 6, 7, 8]
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)
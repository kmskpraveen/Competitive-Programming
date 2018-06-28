import unittest

def contains_check(ordered_list, number, minimum, maximum):

	if maximum >= minimum: 
		mid = minimum + (maximum - minimum)//2

		if ordered_list[mid] == number:
			return True

		elif ordered_list[mid] > number:
			return contains_check(ordered_list, number, minimum, mid-1)

		else:
			return contains_check(ordered_list, number, mid+1, maximum)
 
	else:
		return False

def contains(ordered_list, number):

	# Check if an integer is present in the list

	if len(ordered_list)==0:
		return False

	return contains_check(ordered_list,number,0,len(ordered_list)-1)

















# Tests

class Test(unittest.TestCase):

	def test_empty_list(self):
		result = contains([], 1)
		self.assertFalse(result)

	def test_one_item_list_number_present(self):
		result = contains([1], 1)
		self.assertTrue(result)

	def test_one_item_list_number_absent(self):
		result = contains([1], 2)
		self.assertFalse(result)

	def test_small_list_number_present(self):
		result = contains([2, 4, 6], 4)
		self.assertTrue(result)

	def test_small_list_number_absent(self):
		result = contains([2, 4, 6], 5)
		self.assertFalse(result)

	def test_large_list_number_present(self):
		result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
		self.assertTrue(result)

	def test_large_list_number_absent(self):
		result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
		self.assertFalse(result)

	def test_large_list_number_first(self):
		result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
		self.assertTrue(result)

	def test_large_list_number_last(self):
		result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
		self.assertTrue(result)


unittest.main(verbosity=2)
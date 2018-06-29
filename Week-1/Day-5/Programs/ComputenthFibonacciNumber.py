import unittest


def fib(n):

	# Compute the nth Fibonacci number
	
	low = 0
	high = 1
	total = 0
	if n<0:
		raise Exception
	if n==0:
		return 0
	if n==1:
		return 1

	for i in range(1,n):
		total = low + high
		low = high
		high = total

	return total


















# Tests

class Test(unittest.TestCase):

	def test_zeroth_fibonacci(self):
		actual = fib(0)
		expected = 0
		self.assertEqual(actual, expected)

	def test_first_fibonacci(self):
		actual = fib(1)
		expected = 1
		self.assertEqual(actual, expected)

	def test_second_fibonacci(self):
		actual = fib(2)
		expected = 1
		self.assertEqual(actual, expected)

	def test_third_fibonacci(self):
		actual = fib(3)
		expected = 2
		self.assertEqual(actual, expected)

	def test_fifth_fibonacci(self):
		actual = fib(5)
		expected = 5
		self.assertEqual(actual, expected)

	def test_tenth_fibonacci(self):
		actual = fib(10)
		expected = 55
		self.assertEqual(actual, expected)

	def test_negative_fibonacci(self):
		with self.assertRaises(Exception):
			fib(-1)


unittest.main(verbosity=2)
import unittest


class Stack(object):

	def __init__(self):
		"""Initialize an empty stack"""
		self.items = []

	def push(self, item):
		"""Push new item to stack"""
		self.items.append(item)

	def pop(self):
		"""Remove and return last item"""
		# If the stack is empty, return None
		# (it would also be reasonable to throw an exception)
		if not self.items:
			return None

		return self.items.pop()

	def peek(self):
		"""See what the last item is"""
		if not self.items:
			return None
		return self.items[-1]


class MaxStack(object):

	# Implement the push, pop, and get_max methods
	

	def __init__(self):
		self.List1 = []
		self.List2 = []

	def push(self, item):
		if len(self.List2)==0 or item>=self.List2[len(self.List2)-1]:
			self.List2.append(item)
		self.List1.append(item)

	def pop(self):
		if(self.List1[len(self.List1)-1]==self.List2[len(self.List2)-1]):
			self.List2.pop()
		return self.List1.pop()

	def get_max(self):
		return self.List2[len(self.List2)-1]


















# Tests

class Test(unittest.TestCase):

	def test_stack_usage(self):
		max_stack = MaxStack()

		max_stack.push(5)

		actual = max_stack.get_max()
		expected = 5
		self.assertEqual(actual, expected)

		max_stack.push(4)
		max_stack.push(7)
		max_stack.push(7)
		max_stack.push(8)

		actual = max_stack.get_max()
		expected = 8
		self.assertEqual(actual, expected)

		actual = max_stack.pop()
		expected = 8
		self.assertEqual(actual, expected)

		actual = max_stack.get_max()
		expected = 7	
		self.assertEqual(actual, expected)

		actual = max_stack.pop()
		expected = 7
		self.assertEqual(actual, expected)

		actual = max_stack.get_max()
		expected = 7
		self.assertEqual(actual, expected)

		actual = max_stack.pop()
		expected = 7
		self.assertEqual(actual, expected)

		actual = max_stack.get_max()
		expected = 5
		self.assertEqual(actual, expected)

		actual = max_stack.pop()
		expected = 4
		self.assertEqual(actual, expected)

		actual = max_stack.get_max()
		expected = 5
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)
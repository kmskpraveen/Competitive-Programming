import unittest


class QueueTwoStacks(object):

	# Implement the enqueue and dequeue methods
	List1 = []
	List2 = []
	

	def enqueue(self, item):
		self.List1.append(item)

	def dequeue(self):
		if(len(self.List2)==0):
			while len(self.List1)>0:
				self.List2.append(self.List1.pop())
		return self.List2.pop()


















# Tests

class Test(unittest.TestCase):

	def test_queue_usage(self):
		queue = QueueTwoStacks()

		queue.enqueue(1)
		queue.enqueue(2)
		queue.enqueue(3)

		actual = queue.dequeue()
		expected = 1
		self.assertEqual(actual, expected)

		actual = queue.dequeue()
		expected = 2
		self.assertEqual(actual, expected)

		queue.enqueue(4)

		actual = queue.dequeue()
		expected = 3
		self.assertEqual(actual, expected)

		actual = queue.dequeue()
		expected = 4
		self.assertEqual(actual, expected)

		with self.assertRaises(Exception):
			queue.dequeue()


unittest.main(verbosity=2)
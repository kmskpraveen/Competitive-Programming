import unittest


def find_second_largest(root_node):

	# Find the second largest item in the binary search tree

	previous=None
	current=root_node
	if(current == None):
		raise Exception

	# Loop to go to the right most node of the BST and store it in current
	while(current.right != None):
		previous=current
		current=current.right
	
	# if current has left tree, then we have to find the maximum element in the left sub-tree
	if(current.left != None):
		current=current.left
		# Loop to go to the right most node of the sub tree and store it in current
		while(current.right != None):
			current=current.right	
		previous=current	

	return previous.value














# Tests

class Test(unittest.TestCase):

	class BinaryTreeNode(object):

		def __init__(self, value):
			self.value = value
			self.left = None
			self.right = None

		def insert_left(self, value):
			self.left = Test.BinaryTreeNode(value)
			return self.left

		def insert_right(self, value):
			self.right = Test.BinaryTreeNode(value)
			return self.right

	def test_full_tree(self):
		tree = Test.BinaryTreeNode(50)
		left = tree.insert_left(30)
		right = tree.insert_right(70)
		left.insert_left(10)
		left.insert_right(40)
		right.insert_left(60)
		right.insert_right(80)
		actual = find_second_largest(tree)
		expected = 70
		self.assertEqual(actual, expected)

	def test_largest_has_a_left_child(self):
		tree = Test.BinaryTreeNode(50)
		left = tree.insert_left(30)
		right = tree.insert_right(70)
		left.insert_left(10)
		left.insert_right(40)
		right.insert_left(60)
		actual = find_second_largest(tree)
		expected = 60
		self.assertEqual(actual, expected)

	def test_largest_has_a_left_subtree(self):
		tree = Test.BinaryTreeNode(50)
		left = tree.insert_left(30)
		right = tree.insert_right(70)
		left.insert_left(10)
		left.insert_right(40)
		right_left = right.insert_left(60)
		right_left_left = right_left.insert_left(55)
		right_left.insert_right(65)
		right_left_left.insert_right(58)
		actual = find_second_largest(tree)
		expected = 65
		self.assertEqual(actual, expected)

	def test_second_largest_is_root_node(self):
		tree = Test.BinaryTreeNode(50)
		left = tree.insert_left(30)
		tree.insert_right(70)
		left.insert_left(10)
		left.insert_right(40)
		actual = find_second_largest(tree)
		expected = 50
		self.assertEqual(actual, expected)

	def test_descending_linked_list(self):
		tree = Test.BinaryTreeNode(50)
		left = tree.insert_left(40)
		left_left = left.insert_left(30)
		left_left_left = left_left.insert_left(20)
		left_left_left.insert_left(10)
		actual = find_second_largest(tree)
		expected = 40
		self.assertEqual(actual, expected)

	def test_ascending_linked_list(self):
		tree = Test.BinaryTreeNode(50)
		right = tree.insert_right(60)
		right_right = right.insert_right(70)
		right_right.insert_right(80)
		actual = find_second_largest(tree)
		expected = 70
		self.assertEqual(actual, expected)

	def test_error_when_tree_has_one_node(self):
		tree = Test.BinaryTreeNode(50)
		with self.assertRaises(Exception):
		   find_second_largest(tree)

	def test_error_when_tree_is_empty(self):
		with self.assertRaises(Exception):
		   find_second_largest(None)


unittest.main(verbosity=2)
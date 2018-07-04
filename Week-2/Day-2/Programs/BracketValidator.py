import unittest


def is_valid(code):

	# Determine if the input code is valid

	openersdictionary = {'(': ')','[': ']','{': '}'}

	openers = ['(', '[', '{']
	closers = [')', ']', '}']

	openersList = []

	for i in range(len(code)):

		if (code[i] in openers):
			openersList.append(code[i])
		elif (code[i] in closers):
			if (len(openersList)==0):
				return False
			else:
				if (openersdictionary[openersList.pop(len(openersList)-1)] != code[i]):
					return False
  
	return len(openersList)==0


















# Tests

class Test(unittest.TestCase):

	def test_valid_short_code(self):
		result = is_valid('()')
		self.assertTrue(result)

	def test_valid_longer_code(self):
		result = is_valid('([]{[]})[]{{}()}')
		self.assertTrue(result)

	def test_mismatched_opener_and_closer(self):
		result = is_valid('([][]}')
		self.assertFalse(result)

	def test_missing_closer(self):
		result = is_valid('[[]()')
		self.assertFalse(result)

	def test_extra_closer(self):
		result = is_valid('[[]]())')
		self.assertFalse(result)

	def test_empty_string(self):
		result = is_valid('')
		self.assertTrue(result)


unittest.main(verbosity=2)
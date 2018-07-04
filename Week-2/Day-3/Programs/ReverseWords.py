import unittest


def reverse_words(message):

	# Decode the message by reversing the words

	List = []
	string = ''
	
	for i in range(len(message)):
		if(message[i]!=' '):
			string = string+message[i]
		else:
			List.append(string)
			string = ''

	List.append(string)



	for i in range(len(List)//2):
		temp = List[i]
		List[i] = List[len(List)-i-1]
		List[len(List)-i-1] = temp
	oo = 0

	for i in List:
		for j in i:
			message[oo] = j
			oo += 1
		if(oo!=len(message)):
			message[oo] = ' '
			oo += 1



















# Tests

class Test(unittest.TestCase):

	def test_one_word(self):
		message = list('vault')
		reverse_words(message)
		expected = list('vault')
		self.assertEqual(message, expected)

	def test_two_words(self):
		message = list('thief cake')
		reverse_words(message)
		expected = list('cake thief')
		self.assertEqual(message, expected)

	def test_three_words(self):
		message = list('one another get')
		reverse_words(message)
		expected = list('get another one')
		self.assertEqual(message, expected)

	def test_multiple_words_same_length(self):
		message = list('rat the ate cat the')
		reverse_words(message)
		expected = list('the cat ate the rat')
		self.assertEqual(message, expected)

	def test_multiple_words_different_lengths(self):
		message = list('yummy is cake bundt chocolate')
		reverse_words(message)
		expected = list('chocolate bundt cake is yummy')
		self.assertEqual(message, expected)

	def test_empty_string(self):
		message = list('')
		reverse_words(message)
		expected = list('')
		self.assertEqual(message, expected)


unittest.main(verbosity=2)
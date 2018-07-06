import string
import re
import unittest

class WordCloudData(object):

	# def __init__(self, input_string):

	# 	# Count the frequency of each word
	# 	# print(input_string)
	# 	Listcheck = {}
	# 	s = input_string.lower()
	# 	checkl = "abcdefghijklmnopqrstuvwxyz-'"
	# 	checku = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	# 	# print(input_string)
	# 	count = 0
	# 	self.words_to_counts = {}
	# 	s = ""
	# 	for i in input_string:
	# 		# print(s)
	# 		if i in checku or i in checkl:
	# 			if(i!='.'):
	# 				s = s+i
	# 		else:
	# 			print(s)
	# 			if s!='' and s!='-':
	# 				if s.lower() in [x.lower() for x in self.words_to_counts.keys()]:
	# 					self.words_to_counts[s] += 1
	# 				else:
	# 					self.words_to_counts[s] = 1
	# 			s = ""
	# 	# print(s)
	# 	if s!='':
	# 		if s.lower() in [x.lower() for x in self.words_to_counts.keys()]:
	# 			self.words_to_counts[s] += 1
	# 		else:
	# 			self.words_to_counts[s] = 1



	def __init__(self, input_string):

		ending_points = r"\.|!|\?"
		sentences = re.split(ending_points, input_string)

		self.words_to_counts = {}
		for sentence in sentences:
			words = re.split(r"[^a-zA-Z0-9-']+", sentence)
			for word in words:
				if word != '-':
					self.words_to_counts[word] = self.words_to_counts.get(word, 0) + 1

		def cap_word(word):
			return word[0:1] in string.uppercase

		for word, count in self.words_to_counts.items():
			if cap_word(word) and word.lower() in self.words_to_counts:
				self.words_to_counts[word.lower()] += self.words_to_counts[word]
				del self.words_to_counts[word]

		# return self.words_to_counts
		


















# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

	def test_simple_sentence(self):
		input = 'I like cake'

		word_cloud = WordCloudData(input)
		actual = word_cloud.words_to_counts

		expected = {'I': 1, 'like': 1, 'cake': 1}
		self.assertEqual(actual, expected)

	def test_longer_sentence(self):
		input = 'Chocolate cake for dinner and pound cake for dessert'

		word_cloud = WordCloudData(input)
		actual = word_cloud.words_to_counts

		expected = {
			'and': 1,
			'pound': 1,
			'for': 2,
			'dessert': 1,
			'Chocolate': 1,
			'dinner': 1,
			'cake': 2,
		}
		self.assertEqual(actual, expected)

	def test_punctuation(self):
		input = 'Strawberry short cake? Yum!'

		word_cloud = WordCloudData(input)
		actual = word_cloud.words_to_counts

		expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
		self.assertEqual(actual, expected)

	def test_hyphenated_words(self):
		input = 'Dessert - mille-feuille cake'

		word_cloud = WordCloudData(input)
		actual = word_cloud.words_to_counts

		expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
		self.assertEqual(actual, expected)

	def test_ellipses_between_words(self):
		input = 'Mmm...mmm...decisions...decisions'

		word_cloud = WordCloudData(input)
		actual = word_cloud.words_to_counts

		expected = {'mmm': 2, 'decisions': 2}
		self.assertEqual(actual, expected)

	def test_apostrophes(self):
		input = "Allie's Bakery: Sasha's Cakes"

		word_cloud = WordCloudData(input)
		actual = word_cloud.words_to_counts

		expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)
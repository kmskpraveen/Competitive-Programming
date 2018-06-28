import unittest


class Trie(object):

	# Implement a trie and use it to efficiently store strings
	root = dict()


	def add_word(self, word):

		current_dict = self.root		
		track = 0
		for letter in word:
			if letter in current_dict:
				track += 1
				current_dict = current_dict[letter]
		
		if(track!=len(word)):
			message = True
		else:
			if('end' in current_dict):
				message = False
			else:
				message = True

		current_dict = self.root

		for letter in word:
			current_dict = current_dict.setdefault(letter, {})

		current_dict['end'] = 1

		return message





# {'c': {'a': {'t': {'c': {'h': {'end': 'end'}}}, 'c': {'a': {'k': {'e': {'s': {'end': 'end'}}}}}}}}

# {'c': {'a': {'t': {'c': {'h': {'end': 'end'}}}, 'k': {'e': {'s': {'end': 'end'}}}}}}

# {'c': {'a': {'t': {'c': {'h': {'end': 'end'}}}, 'k': {'e': {'s': {'end': 'end'}, 'end': 'end'}}}}}
 # {'c': {'a': {'t': {'c': {'h': {'end': 1}}}, 'k': {'e': {'s': {'end': 1}, 'end': 2}}}}}


 # {'c': {'a': {'t': {'c': {'h': {'end': 1}}}, 'k': {'e': {'s': {'end': 1}, 'end': 2}}}}}





# Tests

class Test(unittest.TestCase):

	def test_trie_usage(self):
		trie = Trie()

		result = trie.add_word('catch')
		self.assertTrue(result, msg='new word 1')

		result = trie.add_word('cakes')
		self.assertTrue(result, msg='new word 2')

		result = trie.add_word('cake')
		self.assertTrue(result, msg='prefix of existing word')

		result = trie.add_word('cake')
		self.assertFalse(result, msg='word already present')

		result = trie.add_word('caked')
		self.assertTrue(result, msg='new word 3')

		result = trie.add_word('catch')
		self.assertFalse(result, msg='all words still present')

		result = trie.add_word('')
		self.assertTrue(result, msg='empty word')

		result = trie.add_word('')
		self.assertFalse(result, msg='empty word present')

		result = trie.add_word('catched')
		self.assertTrue(result, msg='new word 4')

		result = trie.add_word('catched')
		self.assertFalse(result, msg='word already present')


unittest.main(verbosity=2)
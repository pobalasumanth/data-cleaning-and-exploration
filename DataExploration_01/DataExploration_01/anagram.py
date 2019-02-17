# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 21:45:05 2019

@author: sumanth
"""
def init_words(fname):
	words = {}
	with open(fname) as f:
		for line in f.readlines():
			word = line.strip()
			words[word] = 1
	return words

def init_anagram_dict(words):
	anagram_dict = {}
	for word in words:
		sorted_word = ''.join(sorted(list(word)))
		if sorted_word not in anagram_dict:
			anagram_dict[sorted_word] = []
		anagram_dict[sorted_word].append(word)
	return anagram_dict

def is_anag_frm_dict(word, anagram_dict):
	key = ''.join(sorted(list(word)))
	if key in anagram_dict:
		values = anagram_dict[key]
		# >= 2 garauntees that 'word' is not the only value
		if len(values) >= 2:
			return True
	return False

def get_all_anag_frm_dict(words, anagram_dict):
    anagrams = []
    for word in words:
        if is_anag_frm_dict(word, anagram_dict):
            anagrams.append(word)
    return anagrams

def find_anagrams(word, anagram_dict):
	key = ''.join(sorted(list(word)))
	if key in anagram_dict:
		return set(anagram_dict[key]).difference(set([word]))
	return set([]) 

fname = 'words.txt'
word_dict = init_words(fname)
anagram_dict = init_anagram_dict(word_dict.keys())

allanas = get_all_anag_frm_dict(word_dict, anagram_dict)
print(allanas)
print(find_anagrams('heal', anagram_dict))

'''
#Creating the text file with all the anagrams
with open('all_anagrams.txt', 'w') as f:
    for item in allanas:
        f.write("%s\n" % item)

'''

''' Code to execute the lines for knowing the anagram word for key'''
'''insert the key in my key in 65th line  '''


'''
print(len(allanas)), 'anagrams'
#print(find_anagrams('slap', anagram_dict))
my_key='slicht'
print('the anagrams of ', my_key, 'are', find_anagrams(my_key, anagram_dict))
'''

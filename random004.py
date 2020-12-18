# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:41:59 2020

@author: andrea.baccolini
"""

import random
from random_word import RandomWords
from RandomWordGenerator import RandomWord

r = RandomWords()
r1 = RandomWords()
# r3 = r.get_random_words()
#r2.get_random_word()


# Creating a random word object
rw = RandomWord(constant_word_size=True,
                include_digits=False,
                special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                include_special_chars=False)
print(r1)
print(r)
# print(r3)


nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs")
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")

num1 = random.randrange(0,5)
num2 = random.randrange(0,5)
num3 = random.randrange(0,5)
num4 = random.randrange(0,5)

phrase = nouns[num1] + ' ' + verbs[num2] + ' ' + adv[num3] + ' ' + adj[num4]

# print(phrase)
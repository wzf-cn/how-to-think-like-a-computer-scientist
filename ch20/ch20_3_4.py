# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:58:35 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""

def letters(s):
    my_substitutions = s.maketrans(
      # If you find any of these
      """ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\n!\"#$%&()*“”"+-,./:;<=>?@[]^_`{|}~'\\""",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                              ")
    ns = s.translate(my_substitutions)
    words = ns.split()
    letter_counts = {}
    for i in words:
        letter_counts[i] = letter_counts.get(i, 0) + 1


    return letter_counts
     
f = open('AliceInWonderland.txt')
letter = f.read()
f.close()

letter_counts = letters(letter)
letter_items = list(letter_counts.items())
letter_items.sort()

print('Word{0:<16}Count'.format(' '))
print('=========================')
word_count = open('alice_words', 'w')
word_count.write('Word{0:<16}Count\n'.format(' '))
word_count.write('=========================\n')
for (l, counts) in letter_items:
    print('{0:<20}{1}'.format(l, counts))
    word_count.write('{0:<20}{1}\n'.format(l, counts))
word_count.close()
print('the word "alice" occurs {0} times.'.format(letter_counts['alice']))

longest = 0
for word in letter_counts:
    if len(word) > longest:
        longest = len(word)
        longest_word = word

print('the longest word is {0}, it has {1} characters'.format(longest_word, longest))
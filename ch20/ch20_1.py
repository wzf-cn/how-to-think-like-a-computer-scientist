# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:59:45 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
string = '''Write a program that reads a string and returns 
            a table of the letters of the alphabet in 
            alphabetical! order which occur in the string 
            together with the number of times each letter 
            occurs. Case should be ignored. A sample output 
            of the program when the user enters the data “ThiS 
            is String with Upper and lower case Letters”, would 
            look this this:'''
            
def letters(s):
    my_substitutions = s.maketrans(
      # If you find any of these
      """ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\n!\"#$%&()*“”"+,-./:;<=>?@[]^_`{|}~'\\""",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                              ")
    ns = s.translate(my_substitutions)

    letter_counts = {}
    for i in ns:
        letter_counts[i] = letter_counts.get(i, 0) + 1

    del letter_counts[' ']
    letter_items = list(letter_counts.items())
    letter_items.sort()
    for (l, counts) in letter_items:
        print('{0:<5}{1}'.format(l, counts))
        
letters(string)
letters("ThiS is String with Upper and lower case Letters")

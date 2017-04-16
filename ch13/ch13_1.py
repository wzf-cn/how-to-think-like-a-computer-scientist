# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:01:50 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
Q1:
Write a program that reads a file and writes out a new file with the lines 
in reversed order (i.e. the first line in the old file becomes the last one in 
                   the new file.)
"""
n = open('test.txt', 'r')
f = open('ex1.txt', 'w')

text = n.readlines()
text.reverse()
text2 = text

f.writelines(text2)

n.close()
f.close()
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:11:51 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
Q3:
Write a program that reads a text file and produces an output file which is a 
copy of the file, except the first five columns of each line contain a four 
digit line number, followed by a space. Start numbering the first line in the 
output file at 1. Ensure that every line number is formatted to the same width 
in the output file. Use one of your Python programs as test data for this 
exercise: your output should be a printed and numbered listing of the Python 
program.
"""

f = open('test.txt', 'r')
g = open('new_test.txt', 'w')

i = 1
while True:
    txt = f.readline()
    if len(txt) == 0:
        break
    g.write('{0:<5} '.format(i) + txt[5:])
    i = i+1
    
f.close()
g.close()


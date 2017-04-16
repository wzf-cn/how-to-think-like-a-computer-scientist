# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:14:39 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
Q4:
Write a program that undoes the numbering of the previous exercise: it should 
read a file with numbered lines and produce another file without line numbers.

It looks as same as Q3, so it's just a modification of Q3
"""

f = open('test.txt', 'r')
g = open('new_test.txt', 'w')

i = 1
while True:
    txt = f.readline()
    if len(txt) == 0:
        break
    g.write(txt[5:])
    i = i+1
    
f.close()
g.close()
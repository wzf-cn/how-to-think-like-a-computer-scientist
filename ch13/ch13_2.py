# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:02:21 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
Q2:
Write a program that reads a file and prints only those lines that contain the 
substring snake.
"""

f = open('test.txt', 'r')

while True:
    text = f.readline()
    if len(text) == 0:
        break
    elif text.__contains__('snake'):
        print(text, end = '')

f.close()
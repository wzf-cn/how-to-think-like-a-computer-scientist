# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 19:42:25 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
def count(num, target):
    total = 0
    for i in target:
        if type(i) == type([]):
            total += count(num, i)
        elif i == num:
            total += 1
    return total
from test import *
test(count(2, []), 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]), 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]), 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]), 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]), 6)
test(count('a',
     [['this',['a',['thing','a'],'a'],'is'], ['a','easy']]), 4)
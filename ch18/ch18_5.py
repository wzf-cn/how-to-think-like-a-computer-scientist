# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 19:19:18 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
def recursive_min(l, is_first = True):
    smallest = None
    for num in l:
        if type(num) == type([]):
            val = recursive_min(num)
        else:
            val = num
        
        if is_first or val < smallest:
            smallest = val
            is_first = False
    return smallest

from test import *
test(recursive_min([2, 9, [1, 13], 8, 6]), 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]), 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]), -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]), -13)        
    
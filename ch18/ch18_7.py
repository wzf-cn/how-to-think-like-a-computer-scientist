# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 19:53:43 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
def flatten(lst):
    new_list = []
    for element in lst:
        if type(element) ==type([]):
            new_list.extend(flatten(element))
        else:
            new_list.append(element)
            
    return new_list

from test import *
test(flatten([2,9,[2,1,13,2],8,[2,6]]),[2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]),[9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]),[9,7,1,13,2,8,2,6])
test(flatten([['this',['a',['thing'],'a'],'is'],['a','easy']]),
              ['this','a','thing','a','is','a','easy'])
test(flatten([]), [])
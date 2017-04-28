# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 22:40:40 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
import sys
def re(num = 0, tol_re = 0):
    val = 0

    if val == num:
        print('done! total recursions is {0}'.format(tol_re))
    else:
        print('{0}, '.format(num), end = '')
        re(num-1, tol_re+1)
   
re(100)
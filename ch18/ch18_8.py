# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 19:57:45 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        an_2 = 1
        an_1 = 0
        for i in range(1,num):
            an = an_1 + an_2
            (an_1, an_2) = (an_2, an)
        return an

print(fibonacci(200))
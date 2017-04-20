# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:30:21 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
q_a to q_d does not concern about duplicates
"""

import sys

def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg)
                
def q_a(xs, ys):
    """ a. Return only those items that are present 
        in both lists.
    """
    xi = 0
    yi = 0
    result = []
    
    while True:
        if xi >= len(xs):
            return result
        
        if yi >= len(ys):
            return result
        
        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            result.append(xs[xi])
            xi += 1
            yi += 1

def q_b(xs, ys):
    """ Return only those items that are present in the first
        list, but not in the second.
    """
    xi = 0
    yi = 0
    result = []
    
    while True:
        if xi >= len(xs):
            return result
        
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        else:
            yi += 1

def q_c(xs, ys):
    """ Return only those items that are present in the second
        list, but not in the first.
    """
    return q_b(ys, xs)
    
def q_d(xs, ys):
    """ Return items that are present in either the first or
        the second list.
    """
    xi = 0
    yi = 0
    result = []
    
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            result.append(xs[xi])
            yi += 1
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1
            
def q_e(xs, ys):
    """ Return items from the first list that are not 
        eliminated by a matching element in the second list.
        In this case, an item in the second list “knocks out”
        just one matching item in the first list. This 
        operation is sometimes called bagdiff. For example 
        bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return 
        [5,11,11,12,13]
    """
    xi = 0
    yi = 0
    result = []
    
    while True:
        if xi >= len(xs):
            return result
        
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        else:
            yi += 1

lst1 = [1,2,2,3,5,6,7,8,9]
lst2 = [2,4,6,8,10,12]
test(q_e(lst1, lst2), [1,2,3,5,7,9])
test(q_e([1,2], []), [1,2])
test(q_e([], [1,2]), [])
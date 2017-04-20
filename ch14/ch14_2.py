# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:32:16 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
Q2 Modify the queens program to solve some boards of size 
4, 12, and 16. What is the maximum size puzzle you can usually
solve in under a minute?-------just modify
"""

import sys
import time


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

            
def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True
    
    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False      

def main():
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(14))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found == 0:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1
t0 = time.clock()
main()
t1 = time.clock()
print('it needs {0:.4f} to find the solution'.format(t1 -t0))
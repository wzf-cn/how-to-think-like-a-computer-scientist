# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:14:26 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
Q3:
    Adapt the queens program so that we keep a list of solutions
    that have already printed, so that we don’t print the same 
    solution more than once.
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
    q_list = []
    
    bd = list(range(8))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found <= 10:
       rng.shuffle(bd)
       tries += 1
       if not bd in q_list:
           if not has_clashes(bd):
               print("Found solution {0} in {1} tries.".format(bd, tries))
               q_list.append(bd[:]) # if use q_list.append(bd), that is Aliasing
               tries = 0
               num_found += 1
    q_list.sort()
    print("q_list is: \n")
    for l in q_list:
        print(l)
t0 = time.clock()
main()
t1 = time.clock()
print('it needs {0:.4f} to find the solution'.format(t1 -t0))

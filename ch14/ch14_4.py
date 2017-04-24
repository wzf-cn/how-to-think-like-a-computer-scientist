# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:33:18 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
    Chess boards are symmetric: if we have a solution to the queens problem, 
    its mirror solution — either flipping the board on the X or in the Y axis, 
    is also a solution. And giving the board a 90 degree, 180 degree, or 270
    degree rotation is also a solution. In some sense, solutions that are just
    mirror images or rotations of other solutions — in the same family — are
    less interesting than the unique “core cases”. Of the 92 solutions for the
    8 queens problem, there are only 12 unique families if you take rotations 
    and mirror images into account. Wikipedia has some fascinating stuff about
    this.
    a Write a function to mirror a solution in the Y axis,
    b Write a function to mirror a solution in the X axis,
    c Write a function to rotate a solution by 90 degrees anti-clockwise, 
      and use this to provide 180 and 270 degree rotations too.
    d Write a function which is given a solution, and it generates the family 
      of symmetries for that solution.  For example, the symmetries of
      [0,4,7,5,2,6,1,3] are
      [[0,4,7,5,2,6,1,3],[7,1,3,0,6,4,2,5],
      [4,6,1,5,2,0,3,7],[2,5,3,1,7,4,6,0],
      [3,1,6,2,5,7,4,0],[0,6,4,7,1,3,5,2],
      [7,3,0,2,5,1,6,4],[5,2,4,6,0,3,1,7]]
"""
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


def get_a_solution():
    import random
    rng = random.Random()   # Instantiate a generator
    
    bd = list(range(8))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found ==0:
        tries += 1
        rng.shuffle(bd)
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            num_found += 1
    return bd

def q_a(bd):
    newbd = []
    for value in bd:
        newbd.append(len(bd) - 1 - value)
    return newbd

def q_b(bd):
    bd_x = bd[:]
    bd_x.reverse()
    return bd_x

def q_c(bd):
    bd_t = bd[:]
    for index in range(len(bd)):
        bd_t[len(bd)-1-bd[index]] = index 
    return bd_t

def q_d (bd):
    bd_90 = q_c(bd)
    bd_180 = q_c(bd_90)
    bd_270 = q_c(bd_180)
    print(bd, q_a(bd))
    print(bd_90, q_a(bd_90))
    print(bd_180, q_a(bd_180))
    print(bd_270, q_a(bd_270))

bd = get_a_solution()
bd_y = q_a(bd)
print('for q_a we got:\n{0}'.format(bd_y))

bd_x = q_b(bd)
print('for q_b we got:\n{0}'.format(bd_x))

bd_t = q_c(bd)
print('for q_c we got:\n{0}'.format(bd_t))

    
print('for q_d we got:\n')
q_d(bd)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
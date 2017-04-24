# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:04:27 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width = 0, delta_height = 0):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx = 0, dy = 0):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy
        
    def area(self):     # for Q1
        return self.width * self.height
    
    def perimeter(self):    # for Q2
        return (self.width + self.height) * 2
    
    def flip(self):     # for Q3
        (self.width, self.height) = (self.height, self.width)
        
    def contains(self, p):  # for Q4
        if (p.x >= self.corner.x) and (p.x < (self.width + self.corner.x)):
            if (p.y >= self.corner.y) and (p.y < (self.height + self.corner.y)):
                return True
            else:
                return False
        return False    
        
def is_rec_collide(r1, r2): # find if the 4 points of r2 is in r1
    r2p1 = r2.corner
    r2p2 = Point(r2.corner.x + r2.width, r2.corner.y)
    r2p3 = Point(r2.corner.x, r2.corner.y + r2.height)
    r2p4 = Point(r2.corner.x + r2.width, r2.corner.y + r2.height)
    if r1.contains(r2p1) or r1.contains(r2p1) or r1.contains(r2p3) or r1.contains(r2p4):
        return True
    else:
        return False
        

from test import *

r = Rectangle(Point(0, 0), 10, 5)
test(r.area(), 50)
test(r.perimeter(), 30)
r = Rectangle(Point(100, 50), 10, 5)
test(r.width, 10)
test(r.height, 5)
r.flip()
test(r.width, 5)
test(r.height, 10)
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)), True)
test(r.contains(Point(3, 3)), True)
test(r.contains(Point(3, 7)), False)
test(r.contains(Point(3, 5)), False)
test(r.contains(Point(3, 4.99999)), True)
test(r.contains(Point(-3, -3)), False)
r1 = Rectangle(Point(0, 0), 10, 5)
r2 = Rectangle(Point(10, 1), 1, 2)
test(is_rec_collide(r1, r2), False)
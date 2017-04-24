# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:31:30 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
q_1:
    Rewrite the distance function from the chapter titled 
    Fruitful functions so that it takes two Points as 
    parameters instead of four numbers.
"""

class Point:
    """ Point class represents and manipulates x,y coords."""
    
    def __init__(self, x = 0, y = 0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y
        
    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) **0.5
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
     
    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
   

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

p = Point (0,0)
q = Point(5,12)
print(distance(p,q))
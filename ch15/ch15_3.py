# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:46:26 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
q_3:
    Add a method slope_from_origin which returns the slope of the line joining
    the origin to the point. For example,
    >>> Point(4, 10).slope_from_origin()
    2.5
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
    
    def slope_from_origin(self):
        return self.y / self.x
    
print(Point(4, 10).slope_from_origin())
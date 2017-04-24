# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:51:16 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
q_4:
    The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”).
    The coefficients a and b completely describe the line. Write a method in 
    the Point class so that if a point instance is given another point, it will 
    compute the equation of the straight line joining the two points. It must 
    return the two coefficients as a tuple of two values. For example,
    >>> print(Point(4, 11).get_line_to(Point(6, 15)))
    >>> (2, 3)
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
    
    def get_line_to(self, p):
        a = (self.y - p.y) / (self.x - p.x)
        b = self.y - self.x * a
        return (a, b)
    
print(Point(4, 11).get_line_to(Point(6, 15)))       
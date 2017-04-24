# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:40:31 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
q_2:
    Add a method reflect_x to Point which returns a new Point, one which is 
    the reflection of the point about the x-axis. For example, Point(3, 5).
    reflect_x() is (3, -5)
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
        
    def reflect_x(self):
        self.y = -self.y
        return self

    
p = Point(3,4)
print(p.reflect_x())
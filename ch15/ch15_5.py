# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:57:36 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
q_5:
    Given four points that fall on the circumference of a circle, find the
    midpoint of the circle. When will this function fail?
    Hint: You must know how to solve the geometry problem before you think of 
    going anywhere near programming. You cannot program a solution to a
    problem if you don’t understand what you want the computer to do!
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
    
def mid_of_circle(p1, p2, p3):  # 3 points are enough
    m1 = p1.halfway(p2)   # point m1
    m2 = p2.halfway(p3)   # point m2
    (a1, b1) = p1.get_line_to(p2) # (a1, b1) 
    (a2, b2) = p2.get_line_to(p3) # (a2, b2)
    m_a1 = -1/a1  # -a1
    m_a2 = -1/a2  # -a2
    
    circle_x = ((m2.y - m_a2 * m2.x) - (m1.y - m_a1 * m1.x)) / (m_a1 - m_a2)
    circle_y = m_a1  * (circle_x - m1.x) + m1.y
    
    return Point(circle_x, circle_y)

p1 = Point(0, 5**0.5)
p2 = Point(1, 2)
p3 = Point(2, -1)

print(mid_of_circle(p1,p2,p3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
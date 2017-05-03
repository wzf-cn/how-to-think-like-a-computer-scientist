# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:08:00 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
    
    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours,
                            self.minutes, self.seconds)
    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
    
    def __sub__(self, other):
        return MyTime(0,0, self.to_seconds() - other.to_seconds())
    
    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
            
    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds
            
    def between(self, t2, obj):
        return (self.to_seconds() <= obj.to_seconds() and 
                obj.to_seconds() < t2.to_seconds())
        
from test import *

t1 = MyTime(1,20,50)
t2 = MyTime(6,0,2)
obj1 = MyTime(1,20,51)
obj2 = MyTime(7,15,2)
obj3 = MyTime(1,20,50)

test(t1.between(t2,obj1), True)
test(t1.between(t2,obj2), False)
test(t1.between(t2,obj3), True)
        
        
        
        
        
        
        
        
        
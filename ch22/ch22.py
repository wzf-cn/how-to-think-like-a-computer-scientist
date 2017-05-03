# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:39:00 2017

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
            
def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)

current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
print(current_time-bread_time)
print(current_time+bread_time)


class Point:
    def __init__(self, x1 = 0, x2 = 0):
        self.x = x1
        self.y = x2
        
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other):
        return Point(other * self.x,  other * self.y)
    def reverse(self):
        (self.x , self.y) = (self.y, self.x)    

p1 = Point(3, 4)
p2 = Point(5, 7)
print(p1 * p2)
print(2 * p2)
#print(p2 * 2)

def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))
    
my_list = [1, 2, 3, 4]
front_and_back(my_list)

p = Point(3, 4)
front_and_back(p)



















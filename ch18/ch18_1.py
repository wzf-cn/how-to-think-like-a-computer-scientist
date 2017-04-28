# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:10:52 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
import turtle

def koch(t, order, size):
    if order == 0:
        t.color('red')
        t.forward(size/2)
        t.color('blue')
        t.forward(size/2)

    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)
        
 
    
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('fractals')

t = turtle.Turtle()
t.color('blue')

wn_sz = wn.window_width()/3
od = 2 

t.pensize(3)
t.speed(0)
for i in range(3):
    koch(t, od, wn_sz-100)
    t.left(-120)

wn.mainloop()
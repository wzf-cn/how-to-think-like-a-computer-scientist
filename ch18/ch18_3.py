# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:42:01 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
import turtle

def sierpinski(t, order, size):
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order-1, size/2)
        t.penup()
        t.forward(size/2)
        t.pendown()
        sierpinski(t, order-1, size/2)
        t.penup()
        t.left(120)
        t.forward(size/2)
        t.left(-120)
        t.pendown()
        sierpinski(t, order-1, size/2)
        t.penup()
        t.left(-120)
        t.forward(size/2)
        t.left(120)
        t.pendown()
        
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('fractals')

t = turtle.Turtle()
t.color('blue')
t.speed(0)
t.pensize(3)

wn_sz = wn.window_width()/5
sierpinski(t, 3, wn_sz)
wn.mainloop()

















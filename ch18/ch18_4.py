# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:00:26 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
import turtle

def sierpinski(t, order, size, colorChangeDepth = -1):
    if 0 == colorChangeDepth:
        changeColor(t)
        
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order-1, size/2, colorChangeDepth-1)
        t.penup()
        t.forward(size/2)
        t.pendown()
        sierpinski(t, order-1, size/2, colorChangeDepth-1)
        t.penup()
        t.left(120)
        t.forward(size/2)
        t.left(-120)
        t.pendown()
        sierpinski(t, order-1, size/2, colorChangeDepth-1)
        t.penup()
        t.left(-120)
        t.forward(size/2)
        t.left(120)
        t.pendown()
        
def changeColor(t):
    (old_c, old_fill) = turtle.Turtle.color(t)
    if old_c == 'red':
        t.color('blue')
    elif old_c == 'blue':
        t.color('magenta')
    else:
        t.color('red')
    
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('fractals')

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

wn_sz = wn.window_width()/5
sierpinski(t, 4, wn_sz, 1)
wn.mainloop()

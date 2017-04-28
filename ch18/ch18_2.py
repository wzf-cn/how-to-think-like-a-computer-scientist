# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:51:30 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
import turtle
import math

def cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [-85, 170, -85, 0]: 
            koch(t, order-1, size/2 * (1 - math.sin(math.radians(5))))
            t.left(angle)

def init_turtle(t):
    t.pensize(3)
    t.speed(0)
    t.penup()
    t.left(90)
    t.forward(wn.window_height()/2-20)
    t.left(-90)
    t.backward(wn.window_width()/2-20)
    t.pendown()
    
def ch18_2a():  
    for od in range(4): 
        cesaro(t, od, wn_sz)
        t.penup()
        t.forward(20)
        t.pendown()
    
def ch18_2b_2c():
    for od in range(4): 
        for i in range(4):
            cesaro(t, od, wn_sz)
            t.left(-90)
        t.penup()
        t.forward(wn_sz+20)
        t.pendown()

        
    
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('fractals')

t = turtle.Turtle()
t.color('blue')

wn_sz = wn.window_width()/5

# for 2a
init_turtle(t) 
ch18_2a()

# for 2b
t.penup()
t.backward(4*(wn_sz+20))
t.left(-90)
t.forward(wn_sz+20)
t.left(90)
t.pendown()
ch18_2b_2c()
wn.mainloop()
























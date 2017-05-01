# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:47:54 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
from test import *
def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    
    return

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory, True)
test(new_inventory["strawberries"] == 10, True)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35, True)
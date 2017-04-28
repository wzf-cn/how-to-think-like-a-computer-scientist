# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:45:26 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ''):
    """ Print recursive listing of contents of path """
    if prefix == '':  # Detect outermost call, print a heading
        print('Folder listing for', path)

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(path+'\\'+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname)
            
print_files('C:\my_program\github\how-to-think-like-a-computer-scientist')
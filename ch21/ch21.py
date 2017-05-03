# -*- coding: utf-8 -*-
"""
Created on Mon May  1 23:28:43 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""

 # Crawler crawls the filesystem and builds a dictionary
 # Crawler crawls the filesystem and builds a dictionary
import os
import json

thedict = {}
filecount = 0
def crawl_files(path):
    """ Recursively visit all files in path """
    global filecount
    # Fetch all the entries in the current folder.
    dirlist = os.listdir(path)
    for f in dirlist:
        # Turn each name into full pathname
        fullname = os.path.join(path, f)

        # If it is a directory, recurse.
        if os.path.isdir(fullname):
            crawl_files(fullname)
        else:  # Do something useful with the file
            key = f.lower()  # Normalize the filename
            if key in thedict:
               thedict[key].append(fullname)
            else:   # insert the key and a list of one pathname
               thedict[key] = [fullname]
        filecount += 1
        if filecount % 100 == 0:
            print(".", end="")
            if filecount % 5000 == 0:
                print()
crawl_files("c:\\my_program")
print()  # End the last line of dots ...
print("Indexed {0} files, {1} entries in the dictionary.".
                     format(filecount, len(thedict)))
f = open("C:\\my_program\\github\\how-to-think-like-a-computer-scientist\\ch21\\mydict.txt", "w")
json.dump(thedict, f)
f.close()
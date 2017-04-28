# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:01:38 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
import os
from os.path import join, getsize
for root, dirs, files in os.walk('python/Lib/email'):
    print(root, "consumes", end="")
    print(sum([getsize(join(root, name)) for name in files]), end="")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
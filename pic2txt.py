# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 21:32:18 2018

@author: FanXudong
"""

import os
import re


src = './YOLO/'
path = './YOLO/'


filedir = os.listdir(src)

imgfile = re.compile(r'.*(txt)')
filenamelist = []
for i in filedir:
    if re.match(imgfile, i):
        filenamelist.append(i)

f = open('yolov3.txt','w')

for filename in filenamelist:
    f.write(path + filename + '\n')
f.close()

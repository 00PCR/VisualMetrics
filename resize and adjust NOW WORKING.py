#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:39:30 2021

@author: peterriley
"""

#it is working now


import cv2
import numpy as np
import os

savePath = "/Users/peterriley/Desktop/Trial/"
imagePath =  "/Users/peterriley/Desktop/wheels.png"

def mean2(x):
    y = np.sum(x) / np.size(x);
    return y

newSize = (256, 256)
image = cv2.imread(imagePath)


image = cv2.resize(image, newSize)



imgLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )


imgL = imgLAB[:,:,0]

newMean = 128
newStdev = 32

mean = mean2(imgL)
std = np.std(imgL, ddof=1)
#std = np.std(imgL)
normL = (imgL-mean)/std*newStdev+newMean



imgLAB[:,:,0] = normL

final = cv2.cvtColor(imgLAB, cv2.COLOR_LAB2BGR )


#saving the adjusted image
basename = os.path.basename(imagePath)
cv2.imwrite(os.path.join(savePath + "adjusted " + basename), final)

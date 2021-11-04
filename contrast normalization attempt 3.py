#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:05:18 2021

@author: peterriley
"""

import cv2
import numpy as np

fileName = "/Users/peterriley/Desktop/ABTest/Originals/sunset.jpg"
newSize = (256, 256)
image = cv2.imread(fileName)
image = cv2.resize(image, newSize, interpolation=cv2.INTER_CUBIC)
imgLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )
imgL = imgLAB[:,:,0]

#imgLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )
def global_contrast_normalization(image):

    XX = image
    # replacement for the loop
    X_average = np.mean(XX)
    XX = XX - X_average
    
    ss   = 1.0
    lmda = 10.
    # `su` is here the mean, instead of the sum
    contrast = np.sqrt(lmda + np.mean(XX**2)).astype(np.float64)
    
    if contrast > 1e-8:
        XX = ss * XX / contrast
    else:
        XX = ss * XX 

    return XX

XX = global_contrast_normalization(imgL)
imgLAB[:,:,0] = XX
final = cv2.cvtColor(imgLAB, cv2.COLOR_LAB2BGR )


cv2.imshow("Maybe???", final)
cv2.waitKey(0)
for i in range(4):
    cv2.waitKey(1)
    cv2.destroyAllWindows()
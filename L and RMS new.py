#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:06:51 2021

@author: peterriley
"""

import cv2
import numpy as np
import os
import csv

newSize = (256, 256)
fileName = "/Users/peterriley/Desktop/interstellar.png"

def global_contrast_normalization(final, s, lmda, epsilon):
    #X = cv2.imread(filename)
    X = final

    # replacement for the loop
    X_average = np.mean(X, axis=None)
    print('Mean: ', X_average)
    X = X - X_average

    # `su` is here the mean, instead of the sum
    contrast = np.sqrt(lmda + np.mean(X**2))

    X = s * X / max(contrast, epsilon)
    
    return X

    # scipy can handle it
    #scipy.misc.imsave('result.jpg', X)
 
image = cv2.imread(fileName)
image = cv2.resize(image, newSize, interpolation=cv2.INTER_CUBIC)



imgLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )


imgL = imgLAB[:,:,0]

newMean = 128


mean = np.mean(imgL, axis=None)


normL = imgL-mean+newMean


j, = np.where(normL.ravel()<0) 
normL = normL.ravel()
normL[j] = 0

j = np.where(normL.ravel()>255)
normL = normL.ravel()
normL[j] = 255

normL = np.reshape(normL, newSize)

normL = global_contrast_normalization(normL, 1, 10, 0.000000001) 



imgLAB[:,:,0] = normL

final = cv2.cvtColor(imgLAB, cv2.COLOR_LAB2BGR )





#normImg = np.zeros((256,256))
#normalized = cv2.normalize(image, normImg, 0, 255, cv2.NORM_L2) #cv2.NORM_MINMAX


cv2.imshow("Maybe???", final)
cv2.waitKey(0)
for i in range(4):
    cv2.waitKey(1)
    cv2.destroyAllWindows()
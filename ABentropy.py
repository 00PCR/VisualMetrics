#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:28:10 2021

@author: peterriley
"""

import cv2
import numpy as np

from scipy.stats import entropy

#filename = '/Users/peterriley/Desktop/ABTest/Adjusted/adjusted z winter.jpg'


def ABentropy(filename):
    image= cv2.imread(filename)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )
    
    AB_frame = img[:, :, 1:3]
    
    counts, axis1, axis2 = np.histogram2d(AB_frame[:, :, 0].ravel(), AB_frame[:, :, 1].ravel(), bins =[100, 100])
   
    
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
    
   
   
    counts= counts.flatten()
    
    #adds a little bit to each value to avoid wonkyness of calculating entropy with a lot of 0s
    counts = np.full_like(counts, 0.0001) + counts
    
    #zeros = np.count_nonzero(counts == 0.0001)
    e = entropy(counts, base=2)
    
    return e




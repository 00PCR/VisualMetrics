#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 18:47:27 2021

@author: peterriley
"""

import cv2
import numpy as np

#filename = "/Users/peterriley/Desktop/Background/wheels.png"
def edges(filename):
    gray= cv2.imread(filename)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5), 0) #I assume if we want maximum edges, we'd want to exclude this
    blurred = gray
    wide = cv2.Canny(blurred, 10, 200)
    #two other possible options -- depends on how many edges we want to detect
    #mid = cv2.Canny(blurred, 30, 150)
    #tight = cv2.Canny(blurred, 240, 250)
    edges = np.count_nonzero(wide == 255)
    #an ultimately unnecessary two linesline
    #pixels = gray.shape[0]*gray.shape[0] #gets the total number of pixels. It should be constant but ah , still good to do
    #print(edges/pixels*100)
    return edges

# =============================================================================
# edge = edges(filename)
# print(edge)
# 
# =============================================================================

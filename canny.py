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
   # wide = cv2.Canny(blurred, 10, 200)
    #two other possible options -- depends on how many edges we want to detect
    mid = cv2.Canny(blurred, 30, 150)
   # tight = cv2.Canny(blurred, 240, 250)
# =============================================================================
#     cv2.imshow("a", tight)
#     cv2.waitKey(0)
#     cv2.imshow("b", mid)
#     cv2.waitKey(0)
#     cv2.imshow("c", wide)
#     cv2.waitKey(0)
# =============================================================================
    for i in range(4):
        cv2.waitKey(1)
        cv2.destroyAllWindows()
    
    
    edges = np.count_nonzero(mid == 255)
   
    return edges



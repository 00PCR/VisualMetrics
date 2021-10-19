#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:28:10 2021

@author: peterriley
"""

import cv2
import matplotlib.pyplot as plt

from scipy.stats import entropy

#filename = '/Users/peterriley/Desktop/2.jpg'


def ABentropy(filename):
    image= cv2.imread(filename)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )
    
    AB_frame = img[:, :, 1:3]
    
    counts, axis1, axis2, uh = plt.hist2d(AB_frame[:, :, 0].ravel(), AB_frame[:, :, 1].ravel(), bins =[10, 10])
    # =============================================================================
    # plt.xlabel('A channel (red to green)')
    # plt.ylabel('B channel (yellow to blue)')
    # plt.colorbar()
    # =============================================================================
    
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
    counts= counts.flatten()
    e = entropy(counts, base=2)
    return e




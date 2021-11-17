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


def ABentropy2(filename):
    image= cv2.imread(filename)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )
    
    AB_frame = img[:, :, 1:3]
    
    counts, axis1, axis2 = np.histogram2d(AB_frame[:, :, 0].ravel(), AB_frame[:, :, 1].ravel(), bins =[10, 10])
   
    
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
    
   
   
    counts= counts.flatten()
    
    #adds a little bit to each value to avoid wonkyness of calculating entropy with a lot of 0s
    counts = np.full_like(counts, 0.0001) + counts
    
    #zeros = np.count_nonzero(counts == 0.0001)
    e = entropy(counts, base=2)
    
    return e


def ABentropy(filename, binSize):
    image= cv2.imread(filename)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )
    
    AB_frame = img[:, :, 1:3]
    
    counts, axis1, axis2 = np.histogram2d(AB_frame[:, :, 0].ravel(), AB_frame[:, :, 1].ravel(), bins=binSize, range=[[0,255],[0,255]])
   
    
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
    
    print(len(counts))
   
    counts= counts.flatten()
    
    #adds a little bit to each value to avoid wonkyness of calculating entropy with a lot of 0s
    counts = np.full_like(counts, 0.0001) + counts
    
    #zeros = np.count_nonzero(counts == 0.0001)
    e = entropy(counts, base=2)
    
    return e
# =============================================================================
# 
# import csv
# 
# bins = [2,3,4,5,7,10,15,20,25,50,100]
# 
# paths = "/Users/peterriley/Desktop/ABTest/paths.csv"
# saveName = "/Users/peterriley/Desktop/ABTest/ABbinTestZeros.csv"
# 
# fields = ["path", "2","3", "4", "5", "7", "10", "15", "20", "25", "50", "100"]
# magic = []
#           
# with open(saveName, "w") as new_file:
#             writer = csv.writer(new_file)
#             
#             writer.writerow(fields)
#         
# 
# with open(paths, "r") as csvFile:
#     csv_reader = csv.reader(csvFile)
#     
#     with open(saveName, "a") as new_file:
#         writer = csv.writer(new_file)
#         for i, line in enumerate(csv_reader):
#             magic = []
#             #get the path of the image
#             fileName = line[0]
#             #for i in range
#             for jj in range(len(bins)):
#                 
#                 ent = ABentropy(fileName, bins[jj])
#                 magic.append(ent)
#             
#             writer.writerow([line[0], magic[0], magic[1], magic[2], magic[3], magic[4], magic[5], magic[6], magic[7], magic[8], magic[9], magic[10] 
#                              ])
# 
# 
# 
# =============================================================================


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:39:30 2021

@author: peterriley
"""

#it is not working now


import cv2
import numpy as np
import os
import csv


# =============================================================================
# savePathA = "/Users/peterriley/Desktop/ABTest/Atesting/"
# savePathB = "/Users/peterriley/Desktop/ABTest/Btesting/"
# #imagePath =  "/Users/peterriley/Desktop/wheel.png
# A =  "/Users/peterriley/Desktop/ABTest/paths.csv"
# B = "/Users/peterriley/Desktop/ABTest/AIpaths.csv"
# 
# =============================================================================

A = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/Apaths.csv"
B = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/Bpaths.csv"
C = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/Cpaths.csv"
D = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/Dpaths.csv"
E = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/Epaths.csv"
F = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/Fpaths.csv"
G = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/Gpaths.csv"


savePathA = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/A/"
savePathB = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/B/"
savePathC = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/C/"
savePathD = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/D/"
savePathE = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/E/"
savePathF = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/F/"
savePathG = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/G/"

pathNames = [A, B, C, D, E, F, G]
savePaths = [savePathA, savePathB, savePathC, savePathD, savePathE, savePathF, savePathG]

x = 256 #the new dimensions of the image
newSize = (x, x)

#two things to solve a pesky issue where some paths don't work...even when the image exists
brokenPaths = []
def write_to_csv(paths, savePath):
      with open(savePath, 'w', newline='') as csvfile:
         writer = csv.writer(csvfile)
         
         for i in range(len(paths)):
             writer.writerow([paths[i]])

for i in range(len(pathNames)):
    print("Beginning a new batch")
    with open(pathNames[i], "r") as csvFile:
        csv_reader = csv.reader(csvFile)
        
        for line in csv_reader:
            try:
           
                fileName = line[0]
                image = cv2.imread(fileName)
                
                image = cv2.resize(image, newSize, interpolation=cv2.INTER_CUBIC)
                imgLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB )
                
                
                imgL = imgLAB[:,:,0]
                
                newMean = 128
                newStdev = 32
                #mean = np.mean(imgL, axis=None)
                normL = imgL - np.mean(imgL) / np.std(imgL)*newStdev+newMean
        
        
                j, = np.where(normL.ravel()<0) 
                normL = normL.ravel()
                normL[j] = 0
                
                j = np.where(normL.ravel()>255)
                normL = normL.ravel()
                normL[j] = 255
                
                normL = np.reshape(normL, newSize)
                
                
                
                imgLAB[:,:,0] = normL
                
                final = cv2.cvtColor(imgLAB, cv2.COLOR_LAB2BGR )
        
        
                #saving the adjusted image
                basename = os.path.basename(fileName)
                cv2.imwrite(os.path.join(savePaths[i]+ basename), final)
                
            except:
                fileName = line[0]
                brokenPaths.append(fileName)
                
write_to_csv(brokenPaths, "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/BrokenPaths.csv")


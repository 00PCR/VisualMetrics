#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:04:09 2021

@author: peterriley
"""

# Python program to find files
# recursively using Python


import glob
import csv

#all you need to do is adjust the filePath and savePath and you'll get a csv file of all of the image paths
filePath = "/Volumes/etna/Scholarship/Michelle Greene/Shared/database/SUN900x256/**/*.jpg"
savePath = '/Volumes/Macintosh HD/Users/peterriley/Desktop/VisualMetics/paths.csv'

#remove when actually running the real code
#remove when actually running the real code
#remove when actually running the real code
#remove when actually running the real code
filePath = "/Users/peterriley/Desktop/Background/**/*.png"
savePath = "/Users/peterriley/Desktop/features/paths.csv"

# Returns a list of names in list files.
#print("Using glob.glob()")
files = glob.glob(filePath,
				recursive = True)


def write_to_csv(paths):
      with open(savePath, 'w', newline='') as csvfile:
         writer = csv.writer(csvfile)
         
         for i in range(len(paths)):
             writer.writerow([paths[i]])
        
write_to_csv(files)  



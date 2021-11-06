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
#filePath = "/Volumes/etna/Scholarship/Michelle Greene/Shared/database/SUN900x256/**/*.jpg"
#savePath = '/Volumes/Macintosh HD/Users/peterriley/Desktop/VisualMetics/paths.csv'

#remove when actually running the real code
#remove when actually running the real code
#remove when actually running the real code
#remove when actually running the real code
#filePath = "/Users/peterriley/Desktop/AA/**/*.png"

#filePath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/**/*.jpg"
filePath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/G/**/*.jpg"
savePath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/G/G.csv"

# Returns a list of names in list files.
#print("Using glob.glob()")
files = glob.glob(filePath,
				recursive = True)

files.sort()


def write_to_csv(paths, savePath):
      with open(savePath, 'w', newline='') as csvfile:
         writer = csv.writer(csvfile)
         
         for i in range(len(paths)):
             writer.writerow([paths[i]])
             
write_to_csv(files,savePath)

#used in the initial step to get smaller csv paths
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# =============================================================================
# write_to_csv(files, "/Users/peterriley/Desktop/Deleted/AllPaths.csv")
# a, b, c, d, e, f, g = chunks(files, 18593)
# 
# 
# write_to_csv(a, "/Users/peterriley/Desktop/Deleted/Apaths.csv") 
# write_to_csv(b, "/Users/peterriley/Desktop/Deleted/Bpaths.csv") 
# write_to_csv(c, "/Users/peterriley/Desktop/Deleted/Cpaths.csv") 
# write_to_csv(d, "/Users/peterriley/Desktop/Deleted/Dpaths.csv") 
# write_to_csv(e, "/Users/peterriley/Desktop/Deleted/Epaths.csv") 
# write_to_csv(f, "/Users/peterriley/Desktop/Deleted/Fpaths.csv") 
# write_to_csv(g, "/Users/peterriley/Desktop/Deleted/Gpaths.csv") 
# =============================================================================

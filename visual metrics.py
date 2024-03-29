#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:32:20 2021

@author: peterriley
"""

import csv
import numpy as np

#these are the functions that will actually calcualte the different metrics of visual informatio
import canny #canny.edges(fileName) will return the number of pixels that are edges in the image
import filesize #filesize.filesize(fileName) will return the number of bytes the image is

#bins currently set to 10x10
import ABentropy #ABentropy.ABentropy(fileName) will return the AB entropy

#truthfully this could be a completely seperate aspect. I decided to include it because I wanted to get all the metrics in one swoop (minus the gist descriptor)
#however, it may prove smarter to obtain the npy seperate and just add it in 
import AlexNet2 #AlexNet2.Alexnet(root, outpath, file_names): root = where the images are saved, outpath is where the npy file is saved. file-names is the path.csv file
                #second function" AlexNet2.AlexEntropy(i, data). Returns entropy Data: the npy file, i: index
                
                
                
paths = "/Users/peterriley/Desktop/ABTest/Adjustedpaths.csv" #this is the plain and simple file paths
saveName = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/testing.csv"




fields = ["path", "edge density", "file size (bytes)", "AB entropy", "Alexnet entropy"]



#loads in the AlexNet npy file
#WILL NEED TO CHANGE THIS (it is the outpath + features.npy)
data =  np.load('/Users/peterriley/Desktop/features/features.npy') 


with open(paths, "r") as csvFile:
    csv_reader = csv.reader(csvFile)
    
    with open(saveName, "w") as new_file:
        writer = csv.writer(new_file)
        
        writer.writerow(fields)
    
        for i, line in enumerate(csv_reader):
            
            #get the path of the image
            fileName = line[0]
            
            #run the functions that get different measures of visual information
            edge = canny.edges(fileName)
            size = filesize.filesize(fileName)
            AB = ABentropy.ABentropy(fileName)
            AlexE = AlexNet2.AlexEntropy(i, data)
            

            
            
            writer.writerow([line[0], edge, size, AB, AlexE])
    
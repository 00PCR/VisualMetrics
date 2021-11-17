#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 22:43:04 2021

@author: peterriley
"""

import cv2
import numpy as np
import csv
import random
import os

#THIS ONE WILL CHANGE
# csv of target images
targetCsv = "/Users/peterriley/Desktop/features/VRich.csv"

#csv of all images (will become the other 8 images)
noiseCsv = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/Visual Metrics.csv"

#all of the paths to the original images (provides a means to ensure the same image base category is not the same)
checkCsv = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/OriginalPaths/AllPaths.csv"

with open(targetCsv, "r") as csv_file:
    #create a csv writer object
    csvreader = csv.reader(csv_file)
    next(csv_file)
    targetImages = []
    for line in csvreader:
        targetImages.append(line[0])
    
with open(noiseCsv, "r") as csv_file:
    #create a csv writer object
    csvreader = csv.reader(csv_file)
    next(csv_file)
    noiseImages = []
    for line in csvreader:
        noiseImages.append(line[0])
        
with open(checkCsv, "r") as csv_file:
    #create a csv writer object
    csvreader = csv.reader(csv_file)
    check = []
    for line in csvreader:
        check.append(line[0])
        
#given a full path of a modified image, extract the basename AND determine what its directory is
def magic(fullPath):
    #targetbase is the basename
    targetBase = os.path.basename(fullPath)
    
    #finds the full path to the original image (ie it gets the original pathway with the original file organization)
    matching = [s for s in check if targetBase in s]
    
    #these next two lines actually extract the original image directory
    dirt, targetBase2 = os.path.split(matching[0])
    dirt = os.path.basename(dirt)
    # because why not. In no circumstances should these ever be different
    if targetBase != targetBase2:
        print("Red alert. Something went seriously wrong")
    return targetBase, dirt        


#creates a list of the nine images that will end up becoming the final 3x3 array (and the key)
def imageSelect(targetImage):
    images = []
    images.append(targetImage)
    
    targetBase, targetDirt = magic(targetImage)
    while len(images)<9:
        #generates a random index
        randomIndex = random.randrange(len(noiseImages))
        perhaps = noiseImages[randomIndex]
        noiseBase, noiseDirt = magic(perhaps)
        
        
        # unlikely, but checks to make sure the noise image not from the same folder
        # could change to make sure all of the images are from the same folder (if crazy)
        if targetDirt != noiseDirt:
            images.append(perhaps)
        
        
    random.shuffle(images)
    #beware the zeroing indexing!!!!
    key = images.index(targetImage)
    return images, key


#given an image and a number, puts a border around the image with the number
def BorderLetter(file, number):
    img = cv2.imread(file)
    
    #remove this line in the final version!!!!!!!!!!!!!!!!!!!!
    #img = cv2.resize(img, (256,256), interpolation=cv2.INTER_LINEAR)
    #remove this line in the final version!!!!!!!!!!!!!!!!!!!!
    
    constant=cv2.copyMakeBorder(img,50,20,20,20,cv2.BORDER_CONSTANT,value=[256,256,256] )
    cv2.putText(constant,number,(135,45), 2, 2,(0,0,0), 3, 0)
    return constant

# given nine images, makes the final grid (images must already be read in)
def grid(img1,img2, img3, img4, img5, img6, img7, img8, img9):
    Hori1 = np.concatenate((img1, img2, img3), axis=1)
    Hori2 = np.concatenate((img4, img5, img6), axis=1)
    Hori3 = np.concatenate((img7, img8, img9), axis=1)
    grid = np.concatenate((Hori1, Hori2, Hori3), axis=0)
    return grid

#combined the Border letter and grid functions to produce the final product
#NOTE: this is ~rather sadly~ hard coded (but alas, it does the job it has to). It only works for lists of 9 filenames)
def endProduct(images):
    number = ["1", "2", "3", '4', "5", "6", "7", '8', "9"]
    for i in range(len(images)):
        images[i]=BorderLetter(images[i],number[i])
    final = grid(images[0],images[1],images[2],images[3],images[4],images[5],images[6],images[7],images[8] )
    return final


images, key = imageSelect(targetImages[1])
print("THE KEY IS", key)

#the actual code
noWay = endProduct(images)
cv2.imshow('No  way', noWay)


cv2.waitKey(0)
for i in range(4):
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    



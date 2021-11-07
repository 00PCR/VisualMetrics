#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:54:18 2021

@author: peterriley
"""

import csv
import scipy.io
from scipy.stats import entropy
import csv
import numpy as np

#these are the functions that will actually calcualte the different metrics of visual informatio
import canny #canny.edges(fileName) will return the number of pixels that are edges in the image
import filesize #filesize.filesize(fileName) will return the number of bytes the image is

#bins currently set to 10x10
import ABentropy #ABentropy.ABentropy(fileName) will return the AB entropy

#functionality changed after I already computed the activation energies
import AlexNet2 #AlexNet2.Alexnet(root, outpath, file_names): root = where the images are saved, outpath is where the npy file is saved. file-names is the path.csv file
                #second function" AlexNet2.AlexEntropy(i, data). Returns entropy Data: the npy file, i: index

#the final product!!!
saveName = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/Visual Metrics.csv"




#path to each of the csv files (pre sorted)
Apath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/A/A.csv"
Bpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/B/B.csv"
Cpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/C/C.csv"
Dpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/D/D.csv"
Epath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/E/E.csv"
Fpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/F/F.csv"
Gpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/G/G.csv"



#paths to all of the gist mat files
Agist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/A/Agist.mat"
Bgist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/B/Bgist.mat"
Cgist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/C/Cgist.mat"
Dgist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/D/Dgist.mat"
Egist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/E/Egist.mat"
Fgist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/F/Fgist.mat"
Ggist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/G/Ggist.mat"


#paths to all of the Alexnet npy files
Anpy = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/A/features.npy"
Bnpy = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/B/features.npy"
Cnpy = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/C/features.npy"
Dnpy = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/D/features.npy"
Enpy = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/E/features.npy"
Fnpy = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/F/features.npy"
Gnpy = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/G/features.npy"

#converting each of these into their resespective lists
paths = [Apath, Bpath, Cpath, Dpath, Epath, Fpath, Gpath]
gists = [Agist, Bgist, Cgist, Dgist, Egist, Fgist, Ggist]
npy =   [Anpy, Bnpy, Cnpy, Dnpy, Enpy, Fnpy, Gnpy]

#each of the many fields
fields = ["path", "edge density", "file size (bytes)", "AB entropy", "Alexnet entropy", "Gist entropy"]

with open(saveName, "w") as new_file:
            writer = csv.writer(new_file)
            
            writer.writerow(fields)
            
for j in range(len(paths)):
    print("A new batch has begun...yay!")
    #load in the mat file
    mat = scipy.io.loadmat(gists[j])
    gist = mat["Features"]
    #load in the npy file
    zz = npy[j]
    data = np.load(zz)
    with open(paths[j], "r") as csvFile:
        csv_reader = csv.reader(csvFile)
        
        with open(saveName, "a") as new_file:
            writer = csv.writer(new_file)
            for i, line in enumerate(csv_reader):
                
                #get the path of the image
                fileName = line[0]
               
                edge = canny.edges(fileName)
                size = filesize.filesize(fileName)
                AB = ABentropy.ABentropy(fileName)
                AlexE = AlexNet2.AlexEntropy(i, data)
                
                gistEnt = entropy(gist[:,i], base = 2)
        
            
                writer.writerow([line[0], edge, size, AB, AlexE, gistEnt])
                

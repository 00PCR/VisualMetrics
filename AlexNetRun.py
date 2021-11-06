#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:27:10 2021

@author: peterriley
"""

import AlexNet2

#where the npy file is to be saved
Aoutpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/A/" 
Boutpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/B/"
Coutpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/C/" 
Doutpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/D/" 
Eoutpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/E/" 
Foutpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/F/" 
Goutpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/G/" 



#these are the roots (ie the directories holding the images)
Apath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/A/"
Bpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/B/"
Cpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/C/"
Dpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/D/"
Epath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/E/"
Fpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/F/"
Gpath = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/AdjustedImages/G/"


#csv files of the paths in each file

Acsv ="/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/A/A.csv"
Bcsv ="/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/B/B.csv"
Ccsv ="/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/C/C.csv"
Dcsv ="/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/D/D.csv"
Ecsv ="/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/E/E.csv"
Fcsv ="/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/F/F.csv"
Gcsv ="/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/G/G.csv"


outPaths = [Aoutpath, Boutpath, Coutpath, Doutpath, Eoutpath, Foutpath, Goutpath]

roots = [Apath, Bpath, Cpath, Dpath, Epath, Fpath, Gpath]
csvFiles = [Acsv, Bcsv, Ccsv, Dcsv, Ecsv, Fcsv, Gcsv]


for i in range(len(roots)):
    AlexNet2.Alexnet(roots[i], outPaths[i], csvFiles[i])

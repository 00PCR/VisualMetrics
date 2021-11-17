#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:49:19 2021

@author: peterriley
"""
#something may be wrong with the measures of visual informatino...but hey, at least this code can be applied to whatever version of the matrix is used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os
from shutil import copyfile
import csv

#several weird things to determine
# One --> alexnet entropies (alot are zero. Perhaps re-calculate metrics with this adjusted)
# Two --> why do high and low info levels seems to be switched?
# Three --> close to all black images...

#Sets the top and bottom fraction of images isolated. (currently set low so I have less to work with)
x = 0.00001 

#csv file of visual metrics
file = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/Visual Metrics.csv"
#file = "/Users/peterriley/Desktop/features/testing.csv"

#save paths for the top and bottom ten percent of images
savePathRich = "/Users/peterriley/Desktop/features/VisualRich/"
savePathPoor = "/Users/peterriley/Desktop/features/VisualPoor/"

#save paths for CSV files (path & first PCA)
VHcsv = "/Users/peterriley/Desktop/features/VRich.csv"
VLcsv = "/Users/peterriley/Desktop/features/VPoor.csv"

df=pd.read_csv(file, sep=',',header=None) # reads in the csv file as panda dataframe
temp = df.to_numpy() #converts the dataframe into a numpy array
temp2 = np.delete(temp, 0, axis = 0) #returns an array that has removed the header (probably an easier way to do this but this works)
final = np.delete(temp2, 0, axis=1) #create a version of the array that has the paths removed for PCA analysis

#use these to remove features to see what the PCA is with a subset of features (for testing purposes)
# =============================================================================
# final = final = np.delete(final, 3, axis=1)
# final = final = np.delete(final, 2, axis=1)
# =============================================================================

final = StandardScaler().fit_transform(final) #normalize the data so we don't get anything wonky

paths = temp2[:,0] #pulls just the paths (for indexing later)

#get the variance matrix and plot it (note: 0 for number of components is actually the first component)
pca = PCA().fit(final)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');
variance_matrix = pca.explained_variance_ratio_
print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

#get the first pca for all of the images
pca = PCA(n_components=1)
pca.fit(final)
final_pca = pca.transform(final)
print("original shape:   ", final.shape)
print("transformed shape:", final_pca.shape)


final_pca = np.squeeze(final_pca) #avoids funny business. This makes a 1D matrix

#paths and 1st pca merged together
c = np.column_stack((paths, final_pca))

#determine where the top and bottom decile lay
#currently set super extreme so I only have to look at a couple images

top = np.quantile(final_pca, 1-x)
bottom = np.quantile(final_pca, x)

#extract the top 10% of images
high = np.where(c[:,1]>top)
Vrich  = c[high]
# extract the bottom 10% of images
low = np.where(c[:,1]<bottom)
Vpoor = c[low]

#make a copy of the BOTTOM 10% of images in a new folder
for i in range(len(Vpoor)):
    basename = os.path.basename(Vpoor[i,0])
    copyfile(Vpoor[i,0], savePathPoor+basename)

#make a copy of the TOP 10% of images in a new folder
for i in range(len(Vrich)):
    basename = os.path.basename(Vrich[i,0])
    copyfile(Vrich[i,0], savePathRich+basename)


#save the high and low paths to two seperate csv files for good measure
def write_to_csv(paths, savePath, split):
      with open(savePath, 'w', newline='') as csvfile:
         fields = ["path", "PCA1"]
         writer = csv.writer(csvfile)
         writer.writerow(fields)
         for i in range(len(paths)):
             basename = os.path.basename(paths[i,0])
             writer.writerow([split+basename, paths[i,1]])
             
#CHANEG AT THE END...         
#save high paths
write_to_csv(Vrich, VHcsv, savePathRich)
#save low paths
write_to_csv(Vpoor, VLcsv, savePathPoor)





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:39:40 2021

@author: peterriley
"""

import torch
import thingsvision.vision as vision

from thingsvision.model_class import Model
import csv
from scipy.stats import entropy

# =============================================================================
# 
# root = "/Users/peterriley/Desktop/Background/"    #where the images are stores
# out_path = "/Users/peterriley/Desktop/features/" #where the npy file will be saved
# file_names = "/Users/peterriley/Desktop/features/paths.csv" # a csv of the images that will be used. This prevents values from being inserted into the wrong rows
# =============================================================================


def Alexnet(root, out_path, file_names):

    #this converts the csv file into a list of the paths. This should enable us to process Alexnet in batches without fear anything goes in the wrong row
    with open(file_names, "r") as csv_file:
        #create a csv writer object
        csvreader = csv.reader(csv_file)
        alex = []
        for line in csvreader:
           alex.append(line[0])
            

    model_name = 'alexnet'
    backend = 'pt'
    module_name = "features.7"
    
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = Model(model_name, pretrained=True, model_path=None, device=device, backend="pt")
    
    dl = vision.load_dl(
        root = root,
        out_path = out_path,
        batch_size = 64,
        transforms = model.get_transformations(),
        backend = "pt",
        file_names = alex #this is an added line to dear lord please make sure the values do not get scrambled up
        )
    
    features, targets, probas = model.extract_features(data_loader=dl, module_name=module_name, batch_size=64, flatten_acts=True, clip=False, return_probabilities=True)
    vision.save_features(features, out_path, 'npy')
    
    #no return function because it saves the npy instead

#https://www.frontiersin.org/articles/10.3389/fninf.2021.679838/full
#https://github.com/ViCCo-Group/THINGSvision

def AlexEntropy(i, data):
    data = data[i][:]
    e = entropy(data, base=2)
    return e


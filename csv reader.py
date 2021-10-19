#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:02:18 2021

@author: peterriley
"""
import csv
fileName = "/Users/peterriley/Desktop/features/paths.csv"
#fileName = "/Users/peterriley/Desktop/features/Visual Parameters.csv"

#fields = ["path", "edge density", "file size", "Alexnet", "AB entropy"]

with open(fileName, "r") as csv_file:
    #create a csv writer object
    csvreader = csv.reader(csv_file)
    
    #next(csvreader)
    #csvwriter.writerow(fields) 
    alex = []
    for line in csvreader:
       print(line)
       alex.append(line[0])
        #image = line[0]
    



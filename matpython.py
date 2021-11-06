#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:00:19 2021

@author: peterriley
"""

import scipy.io
import AlexNet2
from scipy.stats import entropy

Agist = "/Volumes/etna/Scholarship/Michelle Greene/Students/Peter Riley/SecretSauce/G/Ggist.mat"
mat = scipy.io.loadmat(Agist)

gist = mat["Features"]


# =============================================================================
# for i in range(len(gist[0,:])):
#     ent = entropy(gist[:,i], base = 2)
#     print(ent)
# =============================================================================

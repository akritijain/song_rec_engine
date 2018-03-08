# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:30:34 2017

@author: Pragya Aneja
"""

import pandas as pd
import numpy as np
import math
name=pd.read_csv("C:/Users/Pragya Aneja/Desktop/SongCSV.csv")
x = np.array(name['Tempo'])
y = np.array(name['Title'])
new_dict = dict(zip(x,y))
list_minimum=[]
def fun(random):
    for i in new_dict.keys():
        z = (i-random)**2
        list_minimum.append(z)
    min_num = min(list_minimum)
    for y in new_dict.keys():
        if(((y-random)**2) == min_num):
            print(new_dict[y])
print(fun(124))


Duration = np.array(name['Duration'])
new_dict_duration = dict(zip(Duration,y))
list_minimum=[]
def fun_duration(random):
    for i in new_dict_duration.keys():
        z = (i-random)**2
        list_minimum.append(z)
    min_num = min(list_minimum)
    for y in new_dict_duration.keys():
        if(((y-random)**2) == min_num):
            print(new_dict_duration[y])
print(fun_duration(230))


KeySignatureConfidence=np.array(name["KeySignatureConfidence"])
new_dict_KeySignatureConfidence = dict(zip(Duration,y))
list_minimum=[]
def fun_KeySignatureConfidence(random):
    for i in new_dict_KeySignatureConfidence.keys():
        z = (i-random)**2
        list_minimum.append(z)
    min_num = min(list_minimum)
    for y in new_dict_KeySignatureConfidence.keys():
        if(((y-random)**2) == min_num):
            print(new_dict_KeySignatureConfidence[y])
print(fun_KeySignatureConfidence(0.5))


TimeSignature=np.array(name["TimeSignature"])
new_dict_TimeSignature = dict(zip(Duration,y))
list_minimum=[]
def fun_TimeSignature(random):
    for i in new_dict_TimeSignature.keys():
        z = (i-random)**2
        list_minimum.append(z)
    min_num = min(list_minimum)
    for y in new_dict_TimeSignature.keys():
        if(((y-random)**2) == min_num):
            print(new_dict_TimeSignature[y])
print(fun_TimeSignature(5))



KeySignature=np.array(name["KeySignature"])
new_dict_KeySignature = dict(zip(Duration,y))
list_minimum=[]
def fun_KeySignature(random):
    for i in new_dict_KeySignature.keys():
        z = (i-random)**2
        list_minimum.append(z)
    min_num = min(list_minimum)
    for y in new_dict_KeySignature.keys():
        if(((y-random)**2) == min_num):
            print(new_dict_KeySignature[y])
print(fun_KeySignature(3))
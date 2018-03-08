# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 04:27:57 2017

@author: Pragya Aneja
"""

def normalize():
    import pandas as pd
    import numpy as np
    
    dataframe = pd.read_csv('SongCSV.csv')
    width = len(dataframe.loc[0, :])
    height = len(dataframe.loc[:,:])
    array = ["Duration", "KeySignature", "KeySignatureConfidence", "Tempo", "TimeSignature", "TimeSignatureConfidence"]
    for i in array:
        temp = i +('_normal')
        std_1 = dataframe.loc[:,i].std()
        mean = dataframe.loc[:,i].mean()
        dataframe[temp] = (dataframe[i]-mean)/std_1

    return dataframe;
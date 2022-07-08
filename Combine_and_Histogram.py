#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:47:52 2021

@author: Mathew
"""


import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# Filename in each folder
filename_contains="Results"

# Where to save overall data:
    
root_path=r"/Users/Mathew/Documents/Current analysis/Lipsomes/Test data/filesforpython/"

pathList=[]     



pathList.append(r"/Users/Mathew/Documents/Current analysis/Lipsomes/Test data/filesforpython/1/")
pathList.append(r"/Users/Mathew/Documents/Current analysis/Lipsomes/Test data/filesforpython/2/")




intensity=[]
intensity_phot=[]

for path in pathList:
  
    
   for root, dirs, files in os.walk(path):
      for name in files:
              # print(name)
              if filename_contains in name:
                
                      resultsname = name
                      print(name)
        
    
                      df=pd.read_table(path+name, sep='\t')

        
   
   
   for i in range(0,len(df)):
       intensity.append(df['Mean'][i])
       intensity_phot.append(((df['Mean'][i])-500)*(0.0272/0.96))
     

np.savetxt(root_path + 'Intensity.csv', intensity,delimiter ="\t")


np.savetxt(root_path + 'Intensity_photons.csv', intensity_phot,delimiter ="\t")


plt.hist(intensity, bins = 50,range=[0,5000], rwidth=0.9,color='#ff0000')
plt.yscale('log')
plt.xlabel('Intensity (ADU)',size=20)
plt.ylabel('Number of Features',size=20)
plt.savefig(root_path+"Int.pdf")
plt.show()

plt.hist(intensity_phot, bins = 50,range=[0,500], rwidth=0.9,color='#ff0000')
plt.yscale('log')
plt.xlabel('Intensity (photons)',size=20)
plt.ylabel('Number of Features',size=20)
plt.savefig(root_path+"Int_photons.pdf")
plt.show()
     
        
    
    
    
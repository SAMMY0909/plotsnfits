import shutil
import csv
import pandas as pd
import fnmatch
import numpy as np
import matplotlib.pyplot as plt
from   astropy.visualization import astropy_mpl_style
from  astropy.io import fits
import os
import glob
import random
import gc
import matplotlib.backends.backend_pdf
import math


#SERI FUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/GALEX_FUV_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfogalexfuv1.txt'))
df = pd.read_csv('countsinfogalexfuv1.txt', sep=',', skipinitialspace=False)
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])

    
#SERI NUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/STACKED_IMAGES_SERI/")
x11=[];y11=[];z11=[];n11=[]
num_lines = sum(1 for line in open('countsinfogalexnuv1.txt'))
df = pd.read_csv('countsinfogalexnuv1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x11.append(df.iat[ctr,0])
    y11.append(df.iat[ctr,1])
    z11.append(df.iat[ctr,2])
    n11.append(df.iat[ctr,3])

y12=[];z12=[]

for ctr1 in range(len(x1)):
    y12.append(abs(y1[ctr1]-y11[ctr1]))
    z12.append(math.sqrt(math.pow(z1[ctr1],2)+math.pow(z11[ctr1],2)))
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/")
plt.figure(num=1, figsize=(8, 6), dpi=1200, facecolor='w', edgecolor='k')
plt.title('GALEX FUV-GALEX NUV VS Sersic Index n',fontsize=15)
plt.ylim(5,0)
plt.xlabel('n:Sersic Index',fontsize=15)
plt.ylabel('$m_{FUV-NUV} $ : FUV-NUV Color',fontsize=15)
plt.grid(False)
plt.errorbar(x1, y12, yerr=z12,fmt='o',color='k',ecolor='k')
for i, txt in enumerate(n11):
    plt.annotate(txt, (x1[i], y12[i]),rotation=90,xytext=((x1[i]+0.03), y12[i]-0.5),fontsize=15)
nm1="fuv-nuv_seri.pdf"
#mm1="fuv-nuv_seri.png"
plt.savefig(nm1)
#plt.savefig(mm1)

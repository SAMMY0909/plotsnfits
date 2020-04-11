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


#MSRB FUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE1_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE1.txt'))
df = pd.read_csv('countsinfoWISE1.txt', sep=',', skipinitialspace=False)
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])

    
#MSRB NUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE3_FITS_6AS/STACKED_IMAGES_MSRB/")
x11=[];y11=[];z11=[];n11=[]
num_lines = sum(1 for line in open('countsinfoWISE3.txt'))
df = pd.read_csv('countsinfoWISE3.txt', sep=',', skipinitialspace=False )
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
plt.title('WISE I - WISE III VS Mean Surface Brightness in KIDS r Band ',fontsize=15)
plt.ylim(1,-0.3)
plt.xlabel('$\mu_{r}$ : Mean Surface Brightness in KIDS-r band',fontsize=15)
plt.ylabel('$m_{W1-W3} $ : WISE I - WISE III Color',fontsize=15)
plt.grid(False)
plt.errorbar(x1, y12, yerr=z12,fmt='o',color='k',ecolor='k')
for i, txt in enumerate(n1):
    plt.annotate(txt, (x1[i], y12[i]),rotation=90,xytext=((x1[i]+0.05),y12[i]-0.12),size=12)
nm1="w1-w3_msrb.pdf"
#mm1="w1-w3_msrb.png"
plt.savefig(nm1)
#plt.savefig(mm1)

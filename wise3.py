import shutil
import csv
import pandas as pd
import fnmatch
import numpy as np
import matplotlib.pyplot as plt
from   astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from  astropy.io import fits
import os
import glob
import random
import gc
#Plot Algorithms using Matplotlib first MSRB and then SERSIC INDEX
#MSRB PLOT
os.chdir("/home/soumyananda/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE3_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE3.txt'))
df = pd.read_csv('countsinfoWISE3.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
plt.figure(num=19, figsize=(6, 4), dpi=1200, facecolor='w', edgecolor='k')
plt.title("WISE-III AB magnitude VS $\mu$ in KIDS r band ")
plt.ylim(8,32)
plt.xlabel('$\mu$ : Mean Surface Brightness- KIDS r band',fontsize=8)
plt.ylabel('$m_{ab} $ : AB Magnitude',fontsize=8)
plt.figtext(0.35,0.85,"#Objects stacked denoted in each bin",fontsize=10)
plt.grid(False)
plt.errorbar(x1, y1, yerr=z1,fmt='.',color='g',ecolor='r')
for i, txt in enumerate(n1):
    plt.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]-3)),fontsize=8)
nm="trend_wise_3_msrb.pdf"
mm="trend_wise_3_msrb.png"
plt.savefig(nm)
plt.savefig(mm)

#SERI PLOT
os.chdir("/home/soumyananda/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE3_FITS_6AS/STACKED_IMAGES_SERI/")
x11=[];y11=[];z11=[];n11=[]
num_lines1 = sum(1 for line1 in open('countsinfoWISE31.txt'))
df1 = pd.read_csv('countsinfoWISE31.txt', sep=',', skipinitialspace=False )
for ctr1 in range(0,num_lines1-1):
    #print(ctr1,df1.iat[ctr1,0],df1.iat[ctr1,1],df1.iat[ctr1,2],df1.iat[ctr1,3])
    x11.append(df1.iat[ctr1,0])
    y11.append(df1.iat[ctr1,1])
    z11.append(df1.iat[ctr1,2])
    n11.append(df1.iat[ctr1,3])
plt.figure(num=20, figsize=(8, 6), dpi=1200, facecolor='w', edgecolor='k')
plt.title('WISE-III AB magnitude VS Sersic Index n',fontsize=8)
plt.ylim(8,32)
plt.xlabel('n:Sersic Index',fontsize=8)
plt.ylabel('$m_{ab} $ : AB Magnitude',fontsize=8)
plt.figtext(0.35,0.85,"#Objects stacked denoted in each bin",fontsize=10)
plt.grid(False)
plt.errorbar(x11, y11, yerr=z11,fmt='.',color='g',ecolor='r')
for i, txt in enumerate(n11):
    plt.annotate(txt, (x11[i], y11[i]),rotation=90,xytext=(x11[i], (y11[i]-3)),fontsize=8)
nm1="trend_wise_3_seri.pdf"
mm1="trend_wise_3_seri.png"
plt.savefig(nm1)
plt.savefig(mm1)

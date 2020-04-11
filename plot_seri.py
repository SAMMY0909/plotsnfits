import shutil
import csv
import pandas as pd
import fnmatch
import numpy as np
import matplotlib.pyplot as plt
from   astropy.visualization import astropy_mpl_style
from   astropy.io import fits
import os
import glob
import random
import gc
import matplotlib.backends.backend_pdf

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6),(ax7,ax8,ax9)) = plt.subplots(3, 3)
#plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)

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
ax1.set_title("GALEX FUV",fontsize=10)
ax1.set_ylim(8,32)
ax1.set_xlabel('n ', fontsize=10)
ax1.set_ylabel('$m_{ab} $ ',fontsize=10)
ax1.spines['right'].set_visible(False) ; ax1.spines['top'].set_visible(False)
ax1.set_xticks([0.7,1.4,2.1,2.8]) ; ax1.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10)
ax1.grid(False)
ax1.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax1.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]-3)),fontsize=10)
    
#SERI NUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfogalexnuv1.txt'))
df = pd.read_csv('countsinfogalexnuv1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax2.set_title("GALEX NUV",fontsize=10)
ax2.set_ylim(8,32)
ax2.set_xlabel('n ', fontsize=10)
ax2.set_ylabel('$m_{ab} $ ',fontsize=10)
ax2.spines['right'].set_visible(False) ; ax2.spines['top'].set_visible(False)
ax2.set_xticks([0.7,1.4,2.1,2.8]) ; ax2.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10) 
ax2.grid(False)
ax2.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax2.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]-3)),fontsize=10)

#SERI SDSS u
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_u_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssu1.txt'))
df = pd.read_csv('countsinfosdssu1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax3.set_title("SDSS u",fontsize=10)
ax3.set_ylim(8,32)
ax3.set_xlabel('n ', fontsize=10)
ax3.set_ylabel('$m_{ab} $ ',fontsize=10)
ax3.spines['right'].set_visible(False) ; ax3.spines['top'].set_visible(False)
ax3.set_xticks([0.7,1.4,2.1,2.8]) ; ax3.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10) 
ax3.grid(False)
ax3.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax3.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]+10)),fontsize=10)

#SERI SDSS g
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_g_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssg1.txt'))
df = pd.read_csv('countsinfosdssg1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax4.set_title("SDSS g",fontsize=10)
ax4.set_ylim(8,32)
ax4.set_xlabel('n ', fontsize=10)
ax4.set_ylabel('$m_{ab} $ ',fontsize=10)
ax4.spines['right'].set_visible(False) ; ax4.spines['top'].set_visible(False)
ax4.set_xticks([0.7,1.4,2.1,2.8]) ; ax4.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10) ; ax4.xaxis.set_ticks_position('bottom')
ax4.grid(False)
ax4.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax4.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]+10)),fontsize=10)
    
#SERI SDSS r
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_r_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssr1.txt'))
df = pd.read_csv('countsinfosdssr1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax5.set_title("SDSS r",fontsize=10)
ax5.set_ylim(8,32)
ax5.set_xlabel('n ', fontsize=10)
ax5.set_ylabel('$m_{ab} $ ',fontsize=10)
ax5.spines['right'].set_visible(False) ; ax5.spines['top'].set_visible(False)
ax5.set_xticks([0.7,1.4,2.1,2.8]) ; ax5.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10) ; ax5.xaxis.set_ticks_position('bottom')
ax5.grid(False)
ax5.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax5.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]+10)),fontsize=10)
    
#SERI SDSS i
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_i_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssi1.txt'))
df = pd.read_csv('countsinfosdssi1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax6.set_title("SDSS i", fontsize=10)
ax6.set_ylim(8,32)
ax6.set_xlabel('n ', fontsize=10)
ax6.set_ylabel('$m_{ab} $ ',fontsize=10)
ax6.spines['right'].set_visible(False) ; ax6.spines['top'].set_visible(False)
ax6.set_xticks([0.7,1.4,2.1,2.8]) ; ax6.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10) ; ax6.xaxis.set_ticks_position('bottom')
ax6.grid(False)
ax6.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax6.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]+10)),fontsize=10)
    
#SERI WISE 1
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE1_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE11.txt'))
df = pd.read_csv('countsinfoWISE11.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax7.set_title("WISE-I",fontsize=10)
ax7.set_ylim(8,32)
ax7.set_xlabel('n ', fontsize=10)
ax7.set_ylabel('$m_{ab} $ ',fontsize=10)
ax7.spines['right'].set_visible(False) ; ax7.spines['top'].set_visible(False)
ax7.set_xticks([0.7,1.4,2.1,2.8]) ; ax7.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10) 
ax7.grid(False)
ax7.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax7.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]-3)),fontsize=10)
    
#SERI WISE 2
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE2_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE21.txt'))
df = pd.read_csv('countsinfoWISE21.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax8.set_title("WISE-II",fontsize=10)
ax8.set_ylim(8,32)
ax8.set_xlabel('n ', fontsize=10)
ax8.set_ylabel('$m_{ab} $ ',fontsize=10)
ax8.spines['right'].set_visible(False) ; ax8.spines['top'].set_visible(False)
ax8.set_xticks([0.7,1.4,2.1,2.8]) ; ax8.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10) 
ax8.grid(False)
ax8.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax8.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]-3)),fontsize=10)
    
#SERI WISE 3
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE3_FITS_6AS/STACKED_IMAGES_SERI/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE31.txt'))
df = pd.read_csv('countsinfoWISE31.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax9.set_title("WISE-III",fontsize=10)
ax9.set_ylim(8,32)
ax9.set_xlabel('n ', fontsize=10)
ax9.set_ylabel('$m_{ab} $ ',fontsize=10)
ax9.spines['right'].set_visible(False) ; ax9.spines['top'].set_visible(False)
ax9.set_xticks([0.7,1.4,2.1,2.8]) ; ax9.set_xticklabels(['0.7','1.4','2.1','2.8'],rotation=0,fontsize=10)
ax9.grid(False)
ax9.errorbar(x1, y1, yerr=z1,fmt='.',color='k',ecolor='k')
for i, txt in enumerate(n1):
    ax9.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (y1[i]-3)),fontsize=10)

os.chdir("/home/seymour/Dropbox/Goswami_REVISED/")
in_pdf="SERI_PLOT.pdf"
#in_png="SERI_PLOT.png"
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.95,hspace=0.7,wspace=0.5)
fig.text(0.85,0.70,"n= SERSIC PROFILE INDEX \n $m_{ab}= $ AB Magnitude",rotation=90,fontsize=11)
fig.savefig(in_pdf, dpi =1200)
#fig.savefig(in_png, dpi =1200)

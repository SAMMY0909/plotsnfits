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
from matplotlib.ticker import ScalarFormatter

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6),(ax7,ax8,ax9)) = plt.subplots(3, 3)
plt.subplots_adjust(top=0.95, bottom=0.10, left=0.10, right=0.90, hspace=0.7,wspace=0.5)

os.chdir("/home/seymour/Dropbox/Goswami_REVISED/CATALOGRADEC_SPLICED/PLOT_PROGS/")
des=[]
df=pd.read_csv('wavelengthlist.txt', sep=',', skipinitialspace=False)
for mn in range(0,9):
	des.append(df.iat[0,mn])
for u in range(0,9):
	print("Wllist",des[u])


#MSRB FUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/GALEX_FUV_FITS_6AS/STACKED_IMAGES_MSRB/")
x11=[];y11=[];z11=[];n11=[]
num_lines = sum(1 for line in open('countsinfogalexfuv.txt'))
df = pd.read_csv('countsinfogalexfuv.txt', sep=',', skipinitialspace=False)
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x11.append(df.iat[ctr,0])
    y11.append(df.iat[ctr,1])
    z11.append(df.iat[ctr,2])
    n11.append(df.iat[ctr,3])

#MSRB NUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/STACKED_IMAGES_MSRB/")
x12=[];y12=[];z12=[];n12=[]
num_lines = sum(1 for line in open('countsinfogalexnuv.txt'))
df = pd.read_csv('countsinfogalexnuv.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x12.append(df.iat[ctr,0])
    y12.append(df.iat[ctr,1])
    z12.append(df.iat[ctr,2])
    n12.append(df.iat[ctr,3])

#MSRB SDSS u
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_u_FITS_6AS/STACKED_IMAGES_MSRB/")
x13=[];y13=[];z13=[];n13=[]
num_lines = sum(1 for line in open('countsinfosdssu.txt'))
df = pd.read_csv('countsinfosdssu.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x13.append(df.iat[ctr,0])
    y13.append(df.iat[ctr,1])
    z13.append(df.iat[ctr,2])
    n13.append(df.iat[ctr,3])

#MSRB SDSS g
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_g_FITS_6AS/STACKED_IMAGES_MSRB/")
x14=[];y14=[];z14=[];n14=[]
num_lines = sum(1 for line in open('countsinfosdssg.txt'))
df = pd.read_csv('countsinfosdssg.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x14.append(df.iat[ctr,0])
    y14.append(df.iat[ctr,1])
    z14.append(df.iat[ctr,2])
    n14.append(df.iat[ctr,3])
    
#MSRB SDSS r
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_r_FITS_6AS/STACKED_IMAGES_MSRB/")
x15=[];y15=[];z15=[];n15=[]
num_lines = sum(1 for line in open('countsinfosdssr.txt'))
df = pd.read_csv('countsinfosdssr.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x15.append(df.iat[ctr,0])
    y15.append(df.iat[ctr,1])
    z15.append(df.iat[ctr,2])
    n15.append(df.iat[ctr,3])

#MSRB SDSS i
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_i_FITS_6AS/STACKED_IMAGES_MSRB/")
x16=[];y16=[];z16=[];n16=[]
num_lines = sum(1 for line in open('countsinfosdssi.txt'))
df = pd.read_csv('countsinfosdssi.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x16.append(df.iat[ctr,0])
    y16.append(df.iat[ctr,1])
    z16.append(df.iat[ctr,2])
    n16.append(df.iat[ctr,3])
    
#MSRB WISE 1
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE1_FITS_6AS/STACKED_IMAGES_MSRB/")
x17=[];y17=[];z17=[];n17=[]
num_lines = sum(1 for line in open('countsinfoWISE1.txt'))
df = pd.read_csv('countsinfoWISE1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x17.append(df.iat[ctr,0])
    y17.append(df.iat[ctr,1])
    z17.append(df.iat[ctr,2])
    n17.append(df.iat[ctr,3])
    
#MSRB WISE 2
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE2_FITS_6AS/STACKED_IMAGES_MSRB/")
x18=[];y18=[];z18=[];n18=[]
num_lines = sum(1 for line in open('countsinfoWISE2.txt'))
df = pd.read_csv('countsinfoWISE2.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x18.append(df.iat[ctr,0])
    y18.append(df.iat[ctr,1])
    z18.append(df.iat[ctr,2])
    n18.append(df.iat[ctr,3])

#MSRB WISE 3
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE3_FITS_6AS/STACKED_IMAGES_MSRB/")
x19=[];y19=[];z19=[];n19=[]
num_lines = sum(1 for line in open('countsinfoWISE3.txt'))
df = pd.read_csv('countsinfoWISE3.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x19.append(df.iat[ctr,0])
    y19.append(df.iat[ctr,1])
    z19.append(df.iat[ctr,2])
    n19.append(df.iat[ctr,3])

s1=[];s2=[];s3=[];s4=[];s5=[];s6=[];s7=[];s8=[];s9=[]
s11=[];s21=[];s31=[];s41=[];s51=[];s61=[];s71=[];s81=[];s91=[]
s1=[y11[0],y12[0],y13[0],y14[0],y15[0],y16[0],y17[0],y18[0],y19[0]]
s2=[y11[1],y12[1],y13[1],y14[1],y15[1],y16[1],y17[1],y18[1],y19[1]]
s3=[y11[2],y12[2],y13[2],y14[2],y15[2],y16[2],y17[2],y18[2],y19[2]]
s4=[y11[3],y12[3],y13[3],y14[3],y15[3],y16[3],y17[3],y18[3],y19[3]]
s5=[y11[4],y12[4],y13[4],y14[4],y15[4],y16[4],y17[4],y18[4],y19[4]]
s6=[y11[5],y12[5],y13[5],y14[5],y15[5],y16[5],y17[5],y18[5],y19[5]]
s7=[y11[6],y12[6],y13[6],y14[6],y15[6],y16[6],y17[6],y18[6],y19[6]]
s8=[y11[7],y12[7],y13[7],y14[7],y15[7],y16[7],y17[7],y18[7],y19[7]]
s9=[y11[8],y12[8],y13[8],y14[8],y15[8],y16[8],y17[8],y18[8],y19[8]]
s11=[z11[0],z12[0],z13[0],z14[0],z15[0],z16[0],z17[0],z18[0],z19[0]]
s21=[z11[1],z12[1],z13[1],z14[1],z15[1],z16[1],z17[1],z18[1],z19[1]]
s31=[z11[2],z12[2],z13[2],z14[2],z15[2],z16[2],z17[2],z18[2],z19[2]]
s41=[z11[3],z12[3],z13[3],z14[3],z15[3],z16[3],z17[3],z18[3],z19[3]]
s51=[z11[4],z12[4],z13[4],z14[4],z15[4],z16[4],z17[4],z18[4],z19[4]]
s61=[z11[5],z12[5],z13[5],z14[5],z15[5],z16[5],z17[5],z18[5],z19[5]]
s71=[z11[6],z12[6],z13[6],z14[6],z15[6],z16[6],z17[6],z18[6],z19[6]]
s81=[z11[7],z12[7],z13[7],z14[7],z15[7],z16[7],z17[7],z18[7],z19[7]]
s91=[z11[8],z12[8],z13[8],z14[8],z15[8],z16[8],z17[8],z18[8],z19[8]]
	
#Pt1
sent1="$\mu_{r}$= "+str(np.round(x11[0],decimals=2))+", $N_{s}$="+str(n11[0])
ax1.set_title(sent1,fontsize=8)
ax1.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax1.set_ylabel('$m_{ab} $ ',fontsize=15)
ax1.set_xscale('log')
ax1.set_ylim(32,8)
ax1.grid(False)
ax1.errorbar(des, s1, yerr=s11,fmt='.',color='k',ecolor='k')
ax1.tick_params(axis='x',labelsize=8,pad=2 )
#Pt2
sent2="$\mu_{r}$= "+str(np.round(x11[1],decimals=2))+", $N_{s}$="+str(n11[1])
ax2.set_title(sent2,fontsize=8)
ax2.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax2.set_ylabel('$m_{ab} $ ',fontsize=15)
ax2.grid(False)
ax2.set_xscale('log')
ax2.set_ylim(32,8)
ax2.errorbar(des, s2, yerr=s21,fmt='.',color='k',ecolor='k')
#Pt3
sent3="$\mu_{r}$= "+str(np.round(x11[2],decimals=2))+", $N_{s}$="+str(n11[2])
ax3.set_title(sent3,fontsize=8)
ax3.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax3.set_ylabel('$m_{ab} $ ',fontsize=15)
ax3.grid(False)
ax3.set_xscale('log')
ax3.set_ylim(32,8)
ax3.errorbar(des, s3, yerr=s31,fmt='.',color='k',ecolor='k')
#Pt4
sent4="$\mu_{r}$= "+str(np.round(x11[3],decimals=2))+", $N_{s}$="+str(n11[3])
ax4.set_title(sent4,fontsize=8)
ax4.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax4.set_ylabel('$m_{ab} $ ',fontsize=15)
ax4.grid(False)
ax4.set_xscale('log')
ax4.set_ylim(32,8)
ax4.errorbar(des, s4, yerr=s41,fmt='.',color='k',ecolor='k')
#Pt5
sent5="$\mu_{r}$= "+str(np.round(x11[4],decimals=2))+", $N_{s}$="+str(n11[4])
ax5.set_title(sent5,fontsize=8)
ax5.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax5.set_ylabel('$m_{ab} $ ',fontsize=15)
ax5.grid(False)
ax5.set_xscale('log')
ax5.set_ylim(32,8)
ax5.errorbar(des, s5, yerr=s51,fmt='.',color='k',ecolor='k')
#Pt6
sent6="$\mu_{r}$= "+str(np.round(x11[5],decimals=2))+", $N_{s}$="+str(n11[5])
ax6.set_title(sent6,fontsize=8)
ax6.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax6.set_ylabel('$m_{ab} $ ',fontsize=15)
ax6.grid(False)
ax6.set_xscale('log')
ax6.set_ylim(32,8)
ax6.errorbar(des, s6, yerr=s61,fmt='.',color='k',ecolor='k')
#Pt7
sent7="$\mu_{r}$= "+str(np.round(x11[6],decimals=2))+", $N_{s}$="+str(n11[6])
ax7.set_title(sent7,fontsize=8)
ax7.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax7.set_ylabel('$m_{ab} $ ',fontsize=15)
ax7.grid(False)
ax7.set_xscale('log')
ax7.set_ylim(32,8)
ax7.errorbar(des, s7, yerr=s71,fmt='.',color='k',ecolor='k')
#Pt8
sent8="$\mu_{r}$= "+str(np.round(x11[7],decimals=2))+", $N_{s}$="+str(n11[7])
ax8.set_title(sent8,fontsize=8)
ax8.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax8.set_ylabel('$m_{ab} $ ',fontsize=15)
ax8.grid(False)
ax8.set_xscale('log')
ax8.set_ylim(32,8)
ax8.errorbar(des, s8, yerr=s81,fmt='.',color='k',ecolor='k')
#Pt9
sent9="$\mu_{r}$= "+str(np.round(x11[8],decimals=2))+", $N_{s}$="+str(n11[8])
ax9.set_title(sent9,fontsize=8)
ax9.set_xlabel(r'$log(\lambda(\AA))$', fontsize=12)
ax9.set_ylabel('$m_{ab} $ ',fontsize=15)
ax9.grid(False)
ax9.set_xscale('log')
ax9.set_ylim(32,8)
ax9.errorbar(des, s9, yerr=s91,fmt='.',color='k',ecolor='k')



os.chdir("/home/seymour/Dropbox/Goswami_REVISED/")
in_pdf="SED_MSRB_PLOT.pdf"
#in_png="SED_MSRB_PLOT.png"
fig.text(0.95,0.85,"$\mu_{r}$= Mean Surface Brightness in KIDS r Band, $N_s$= Sample Size in each bin \n $m_{ab}= $ AB Magnitude; Wavelength in Angstorms is in logarithmic scale",rotation=90,fontsize="8")
#fig.tight_layout()
fig.savefig(in_pdf, dpi =1200)
#fig.savefig(in_png, dpi =1200)

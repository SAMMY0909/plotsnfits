import pandas as pd
import matplotlib.pyplot as plt
import os

fig, ax = plt.subplots()
ax.set_title("Combined ab Magnitude vs Mean Surface Brightness in KIDS r Band Plot",fontsize=15)
ax.set_ylim(35,8)
ax.set_xlabel('$\mu_{r}$ ', fontsize=15)
ax.set_ylabel('$m_{ab} $ ',fontsize=15)

#MSRB FUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/GALEX_FUV_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfogalexfuv.txt'))
df = pd.read_csv('countsinfogalexfuv.txt', sep=',', skipinitialspace=False)
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='*',color='0.1',ecolor='k',label='GALEX FUV')
for i, txt in enumerate(n1):
    ax.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (10)),fontsize=15)
    
#MSRB NUV
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfogalexnuv.txt'))
df = pd.read_csv('countsinfogalexnuv.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='*',color='0.4',ecolor='k', label='GALEX NUV')

#MSRB SDSS u
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_u_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssu.txt'))
df = pd.read_csv('countsinfosdssu.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.1',ecolor='k',label='SDSS u')

#MSRB SDSS g
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_g_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssg.txt'))
df = pd.read_csv('countsinfosdssg.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.4',ecolor='k',label='SDSS g')

    
#MSRB SDSS r
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_r_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssr.txt'))
df = pd.read_csv('countsinfosdssr.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.7',ecolor='k',label='SDSS r')
   
#MSRB SDSS i
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/SDSS_i_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfosdssi.txt'))
df = pd.read_csv('countsinfosdssi.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.9',ecolor='k',label='SDSS i')
   
#MSRB WISE 1
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE1_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE1.txt'))
df = pd.read_csv('countsinfoWISE1.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='+',color='0.1',ecolor='k',label='WISE2')

#MSRB WISE 2
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE2_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE2.txt'))
df = pd.read_csv('countsinfoWISE2.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='+',color='0.4',ecolor='k',label='WISE2')

#MSRB WISE 3
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/DATA_FITS_KIDS_GAMA_VST/WISE3_FITS_6AS/STACKED_IMAGES_MSRB/")
x1=[];y1=[];z1=[];n1=[]
num_lines = sum(1 for line in open('countsinfoWISE3.txt'))
df = pd.read_csv('countsinfoWISE3.txt', sep=',', skipinitialspace=False )
for ctr in range(0,num_lines-1):
    #print(ctr,df.iat[ctr,0],df.iat[ctr,1],df.iat[ctr,2],df.iat[ctr,3])
    x1.append(df.iat[ctr,0])
    y1.append(df.iat[ctr,1])
    z1.append(df.iat[ctr,2])
    n1.append(df.iat[ctr,3])
ax.errorbar(x1, y1, yerr=z1,fmt='+',color='0.7',ecolor='k',label="WISE3")
ax.legend(loc='center left',bbox_to_anchor=(1,0.5))
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/")
in_pdf="MSRB_COMBINED_PLOT.pdf"
#in_png="MSRB_COMBINED_PLOT.png"
#plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9,hspace=0.7,wspace=0.5)
#fig.text(0.93,0.70,"$\mu_{r}$= Mean Surface Brightness in KIDS r Band \n $m_{ab}= $ AB Magnitude, Numbers on top denote binning size",rotation=90,fontsize="8")
fig.savefig(in_pdf, dpi =1200,bbox_inches='tight')
#fig.savefig(in_png, dpi =1200)

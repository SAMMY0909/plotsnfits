import pandas as pd
import matplotlib.pyplot as plt
import os

fig, ax = plt.subplots()
ax.set_title("Combined ab Magnitude vs Sersic Index Plot",fontsize=15)
ax.set_ylim(35,8)
ax.set_xlabel('n', fontsize=15)
ax.set_ylabel('$m_{ab} $ ',fontsize=15)

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
ax.errorbar(x1, y1, yerr=z1,fmt='*',color='0.1',ecolor='k',label='GALEX FUV')
for i, txt in enumerate(n1):
    ax.annotate(txt, (x1[i], y1[i]),rotation=90,xytext=(x1[i], (10)),fontsize=15)
    
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
ax.errorbar(x1, y1, yerr=z1,fmt='*',color='0.4',ecolor='k', label='GALEX NUV')

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
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.1',ecolor='k',label='SDSS u')

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
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.4',ecolor='k',label='SDSS g')

    
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
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.9',ecolor='k',label='SDSS r')
   
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
ax.errorbar(x1, y1, yerr=z1,fmt='o',color='0.75',ecolor='k',label='SDSS i')
   
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
ax.errorbar(x1, y1, yerr=z1,fmt='+',color='0.1',ecolor='k',label='WISE2')

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
ax.errorbar(x1, y1, yerr=z1,fmt='+',color='0.4',ecolor='k',label='WISE2')

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
ax.errorbar(x1, y1, yerr=z1,fmt='+',color='0.7',ecolor='k',label="WISE3")
ax.legend(loc='center left',bbox_to_anchor=(1,0.5))
os.chdir("/home/seymour/Dropbox/Goswami_REVISED/")
in_pdf="SERI_COMBINED_PLOT.pdf"
#in_png="SERI_COMBINED_PLOT.png"
#plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9,hspace=0.7,wspace=0.5)
#fig.text(0.93,0.70,"n= Sersic Index \n $m_{ab}= $ AB Magnitude, Numbers on top denote binning size",rotation=90,fontsize="8")
fig.savefig(in_pdf, dpi =1200,bbox_inches='tight')
#fig.savefig(in_png, dpi =1200)

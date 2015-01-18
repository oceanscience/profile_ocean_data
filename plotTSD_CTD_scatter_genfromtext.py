#============================================================================
# Reads text tab delimited data file with a header using "genfromtxt" function from NumPy Library
# Plots using the "scatter" plot function in Matplotlib library.  
# Plots CTD Temp-Sal-Depth data scatter plots with colormap and colorbar. 
# All data read is plotted on the same plot, does not make one plot per file.
#
#  Created By:   Diana Cardoso, Bedford Institute of Oceangraphy
#                Diana.Cardoso@dfo-mpo.gc.ca
#		  
#============================================================================
#- Module imports:
import matplotlib.pyplot as plt
import glob
import numpy as np
import numpy.ma as ma

#- Get CTD data file names for HUD2014017 cruise
files = [f for f in glob.iglob('*.cnv')] # generator, search immediate subdirectories 
print files

#- Load T-S-P CTD data for HUD2014017 cruise has 384 lines of header
x1=[]
y1=[]
z1=[]
for idx, filename in enumerate(files):

    data= np.genfromtxt(filename, skip_header=384,usecols = (2, 3, 15) )  #delimiter='\t'
    #print data.shape
    x=data[0:-1,2]
    y=data[0:-1,1]
    z=data[0:-1,0]
    x1=np.append(x1,x)
    y1=np.append(y1,y)
    z1=np.append(z1,z)

#- Get CTD data file names for HUD2013021 cruise has 388 lines of header
files2 = [g for g in glob.iglob('*.CNV')] # generator, search immediate subdirectories 
print files2

#- Load T-S-P CTD data for HUD2013021 cruise
for idx, filename in enumerate(files2):

    data= np.genfromtxt(filename, skip_header=388,usecols = (2, 3, 15) )  #delimiter='\t'
    #print data.shape
    x=data[0:-1,2]
    y=data[0:-1,1]
    z=data[0:-1,0]
    x1=np.append(x1,x)
    y1=np.append(y1,y)
    z1=np.append(z1,z)
    
x1m=ma.masked_greater_equal(x1, 35.2)

#- Plot T-S diagram for data in all files
plt.figure(1)
plt.scatter(x1m,y1, s=10, c=z1, edgecolor='None')
plt.ylabel('Temperature [$^\circ$C]')
plt.xlabel('Salinity [PSU]')
plt.title("Temperature-Salinity, Cruise #, Cast # to #, July 2014")
cbar = plt.colorbar()
cbar.set_label('Depth [m]')

#- Call show and savefig:
plt.savefig('TSD-scatterplot.png')
plt.show()
plt.close()


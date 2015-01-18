#============================================================================
# Reads text tab delimited data file with no header using "open" built in python function
# Plots using the "scatter" plot function in Matplotlib library.  
# Plots CTD Temp-Sal-Depth data scatter plots with color map and Temp and Sal CTD data scatter profile plots. 
# All data read is plotted on the same plot, does not make one plot per file.
#
#  Created By:   Diana Cardoso, Bedford Institute of Oceangraphy
#                Diana.Cardoso@dfo-mpo.gc.ca
#		  
#============================================================================
#- Module imports:
import matplotlib.pyplot as plt
import numpy as np
import glob

#- Get CTD data file names
files = [f for f in glob.iglob('*.cnv')] # generator, search immediate subdirectories 
print files

#- Load T-S-P CTD data
x1=[]
y1=[]
z1=[]
for idx, filename in enumerate(files):

	f=open(filename,'r')
	lines = f.readlines()
	f.close() 
	for line in lines:
		p=line.split()
		x1.append(float(p[16]))
		y1.append(float(p[3]))
		z1.append(float(p[2]))
		
#- Plot T profile for data in all files
plt.figure(1)
plt.scatter(y1,z1, marker=u'.')
axes = plt.gca()
axes.set_ylim([0,3000])
axes.invert_yaxis()
plt.xlabel('Temperature [$^\circ$C]')
plt.ylabel('Pressure [db]')
plt.title("CTD Temperature")
#- Call show and savefig:
plt.savefig('T-scatterplot.png')
plt.show()
plt.close()

#- Plot S profile for data in all files
plt.figure(2)
plt.scatter(x1,z1, marker=u'.')
axes = plt.gca()
axes.set_ylim([0,3000])
axes.invert_yaxis()
plt.xlabel('Salinity [$^\circ$C]')
plt.ylabel('Pressure [db]')
plt.title("CTD Salinity")
#- Call show and savefig:
plt.savefig('S-scatterplot.png')
plt.show()
plt.close()

#- Plot T S scatter profile for data in all files
plt.figure(3)
plt.scatter(x1,y1,s=10,c=z1, edgecolor='None')
cbar = plt.colorbar()
cbar.set_label('Depth [m]')
plt.xlabel('Salinity [$^\circ$C]')
plt.ylabel('Temperature [$^\circ$C]')
plt.title("CTD Temperature-Salinity")
#- Call show and savefig:
plt.savefig('TS-scatterplot.png')
plt.show()
plt.close()

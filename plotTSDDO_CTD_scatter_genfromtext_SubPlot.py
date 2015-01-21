#============================================================================
# T-S plot, T and S profile plots of CTD data with headers
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
#print files

#- Load T-S-P CTD data for HUD2014017 cruise has 384 lines of header
s1=[]
t1=[]
z1=[]
d1=[]
o1=[]
for idx, filename in enumerate(files):

    data= np.genfromtxt(filename, skip_header=384,usecols = (2, 3, 15, 19, 21) )  #delimiter='\t'
    #print data.shape
    o=data[0:-1,4]
    d=data[0:-1,3]
    s=data[0:-1,2]
    t=data[0:-1,1]
    z=data[0:-1,0]

    s1=np.append(s1,s)
    t1=np.append(t1,t)
    z1=np.append(z1,z)
    d1=np.append(d1,d)
    o1=np.append(o1,o)
    
#- Get CTD data file names for HUD2013021 cruise has 388 lines of header
files2 = [g for g in glob.iglob('*.CNV')] # generator, search immediate subdirectories 
#print files2

#- Load T-S-P CTD data for HUD2013021 cruise
for idx, filename in enumerate(files2):

    data= np.genfromtxt(filename, skip_header=388,usecols = (2, 3, 15, 19, 21) )  #delimiter='\t'
    #print data.shape
    o=data[0:-1,4]
    d=data[0:-1,3]
    s=data[0:-1,2]
    t=data[0:-1,1]
    z=data[0:-1,0]

    s1=np.append(s1,s)
    t1=np.append(t1,t)
    z1=np.append(z1,z)
    d1=np.append(d1,d)
    o1=np.append(o1,o)
    
s1m=ma.masked_greater_equal(s1, 35.2)
d1m=ma.masked_greater_equal(d1, 28.2)
o1m=ma.masked_less_equal(o1, 2)

#- Plot T Profile diagram for data in all files
plt.figure(1)
plt.subplot(2,2,1)
plt.scatter(t1, z1, marker=u'.')
plt.ylabel('Depth [m]')
axes = plt.gca()
axes.set_ylim([0,3000])
axes.invert_yaxis()
#axes.xaxis.set_tick_params(labeltop='on') #label both axis of plot
axes.yaxis.set_label_coords(-0.2, -0.2, transform=None)
#axes.xaxis.tick_top() #ticks only on the top
axes.xaxis.set_ticks_position("both")
axes.xaxis.set_label_position("top") 
axes.set_xlabel('Temperature [$^\circ$C]')
plt.setp(axes.get_xticklabels(), fontsize=10) #rotation='vertical'
plt.setp(axes.get_yticklabels(), fontsize=10)

#- Plot S Profile diagram for data in all files
plt.subplot(2,2,2)
plt.scatter(s1m, z1, marker=u'.')
axes = plt.gca()
axes.set_ylim([0,3000])
axes.invert_yaxis()
axes.yaxis.set_ticklabels([])
axes.xaxis.set_ticks_position("both")
axes.xaxis.set_label_position("top") 
axes.set_xlabel('Salinity [PSU]')
plt.setp(axes.get_xticklabels(), fontsize=10) #rotation='vertical'
plt.setp(axes.get_yticklabels(), fontsize=10)

#- Plot D Profile diagram for data in all files
plt.subplot(2,2,3)
plt.scatter(d1m, z1, marker=u'.')
axes = plt.gca()
axes.set_ylim([0,3000])
axes.invert_yaxis()
axes.xaxis.set_ticks_position("both")
axes.xaxis.set_label_position("top") 
axes.set_xlabel('sigma-theta, [Kg $m^{-3}$]')
plt.setp(axes.get_xticklabels(), fontsize=10) #rotation='vertical'
plt.setp(axes.get_yticklabels(), fontsize=10)

#- Plot O Profile diagram for data in all files
plt.subplot(2,2,4)
plt.scatter(o1m, z1, marker=u'.')
axes = plt.gca()
axes.set_ylim([0,3000])
axes.invert_yaxis()
axes.yaxis.set_ticklabels([])
axes.xaxis.set_ticks_position("both")
axes.xaxis.set_label_position("top") 
axes.set_xlabel('Oxygen [ml $l^{-1}$]')
plt.setp(axes.get_xticklabels(), fontsize=10) #rotation='vertical'
plt.setp(axes.get_yticklabels(), fontsize=10)

#- Call show and savefig:
plt.savefig('TSDO-scatterplot_bothcruise.png')
plt.show()
#plt.close()
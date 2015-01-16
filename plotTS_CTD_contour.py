#============================================================================
# T and S contour plots of CTD data
#
#  Created By:   Diana Cardoso, Bedford Institute of Oceangraphy
#                Diana.Cardoso@dfo-mpo.gc.ca
#		  
#============================================================================
#- Module imports:
import matplotlib.pyplot as plt
import numpy as np
import glob
from matplotlib.mlab import griddata

#- Get CTD data file names
files = [f for f in glob.iglob('*.cnv')] # generator, search immediate subdirectories 
print files

#- Load T-S-P CTD data
s=[]
t=[]
z=[]
for idx, filename in enumerate(files): # load all data into one array for each variable
	f=open(filename,'r')
	lines = f.readlines()
	f.close() 
	for line in lines:
		p=line.split()
		s.append(float(p[16]))
		t.append(float(p[3]))
		z.append(float(p[2]))

dict_s={}
dict_t={}
dict_z={}
dict_lat={}
dict_lon={}

for idx, filename in enumerate(files):# load all data into a dictionary each cast having its own array
	s1=[]
	t1=[]
	z1=[]
	lat=[]
	lon=[]
	f=open(filename,'r')
	lines = f.readlines()
	f.close() 
	for line in lines:
		p=line.split()
		s1.append(float(p[16]))
		t1.append(float(p[3]))
		z1.append(float(p[2]))
		lat.append(float(p[13]))
		lon.append(float(p[14]))
	dict_s['s%i' %idx]=np.array(s1)
	dict_t['t%i' %idx]=np.array(t1)
	dict_z['z%i' %idx]=np.array(z1)
	dict_lat['l%i' %idx]=np.array(lat)
	dict_lon['l%i' %idx]=np.array(lon)
	

# Find mean Lat and lon and max depth for each cast	
latm= np.zeros(len(dict_s))
lonm= np.zeros(len(dict_s))
zmax=np.zeros(len(dict_s))
for i in range(len(dict_s)):
	latm[i]=sum(dict_lat['l%i' %i])/len(dict_lat['l%i' %i])
	lonm[i]=sum(dict_lon['l%i' %i])/len(dict_lon['l%i' %i])
	zmax[i]=max(dict_z['z%i' %i])
print latm
print lonm
print zmax
ymax=int(round(max(zmax)+100)) #max depth for all casts
print ymax

# calculate distance between two points on earth's surface given by their latitude-longitude pair.
yi=range(0,ymax,5)
yii=np.array(yi)
x0=np.arange(lonm[0], lonm[-1],0.01)
k=np.polyfit(lonm, latm, 1)
print k
y0 = k[0]*x0 + k[1]
xref  = x0[0]
yref  = y0[0]
dy20  = np.square(y0-yref)
dx20  = np.square((x0-xref)*np.cos(0.5*(y0-yref)*3.1415/180))
ds0   = 110.585*np.sqrt(dy20 + dx20)
dy2  = np.square(latm-yref)
dx2  = np.square((lonm-xref)*np.cos(0.5*(latm-yref)*3.1415/180))
ds   = 110.585*np.sqrt(dy2 + dx2) #distance between each cast in km
print ds

xi=range(0, int(round(ds[-1]))+1,1)
xii=np.array(xi)

# create an array of distances for each cast
dist=[]
for i in range(len(dict_s)):
	sizet=np.ones(len(dict_lat['l%i' %i]))
	at=sizet*ds[i]
	dist.extend(at)

# interpolate to a regular grid using grid data 
Tgrid = griddata(dist,z,t,xii,yii) 
Sgrid = griddata(dist,z,s,xii,yii) 

# Contour Plots
f=plt.figure()
ax=f.add_axes([.125,.1,.775,.8])
cax=ax.pcolor(xii,yii,Tgrid, cmap=plt.cm.jet)
cs=ax.contour(xii,yii,Tgrid, colors='0.60',lw=0.5) #V=[1, 4, 6]
ax.clabel(cs, fontsize=10, fmt='%d')
ax.plot(ds,np.ones(len(ds)),marker=u'v',color='k',markersize=15)
ax.invert_yaxis()
cbar = plt.colorbar(cax,ax=ax)
cbar.set_label('Temperature [$^\circ$C]')
ax.set_xlabel('Distance [km] ')
ax.set_ylabel('Depth [m]')
ax.set_title("Temperature, Cruise Hudson2014017, Cast 25 to 31, July 2014")

#- Call show and savefig:
f.savefig('T-contourplot.png')
f.show()
plt.close(f)

f=plt.figure()
ax=f.add_axes([.125,.1,.775,.8])
cax=ax.pcolor(xii,yii,Sgrid, cmap=plt.cm.jet)
cs=ax.contour(xii,yii,Sgrid, colors='0.60',lw=0.5) #V=[1, 4, 6]
ax.clabel(cs, fontsize=10, fmt='%2.1f')
ax.plot(ds,np.ones(len(ds)),marker=u'v',color='k',markersize=15)
ax.invert_yaxis()
cbar = plt.colorbar(cax,ax=ax)
cbar.set_label('Salinity [PSU]')
ax.set_xlabel('Distance [km] ')
ax.set_ylabel('Depth [m]')
ax.set_title("Salinity, Cruise Hudson2014017, Cast 25 to 31, July 2014")

#- Call show and savefig:
plt.savefig('S-contourplot.png')
plt.show()
plt.close(f)

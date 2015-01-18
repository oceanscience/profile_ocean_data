#============================================================================
# T and S and D profile plots of CTD data
#
#  Created By:   Diana Cardoso, Bedford Institute of Oceangraphy
#                Diana.Cardoso@dfo-mpo.gc.ca
#		  
#============================================================================
#- Module imports:
import matplotlib.pyplot as plt
import numpy as np

#- Load, plot, save and show profile of T-S-D CTD data
plt.plotfile('d017a025.cnv',cols = (3,2), delimiter=' ', linestyle='None',marker ='.', color ='b',checkrows = 0)
plt.gca().invert_yaxis()
plt.plotfile('d017a026.cnv',cols = (3,2), delimiter=' ', linestyle='None', marker ='.', color ='k',checkrows = 0, newfig=False)
plt.plotfile('d017a027.cnv',cols = (3,2), delimiter=' ', linestyle='None', marker ='.', color ='g',checkrows = 0, newfig=False)
plt.plotfile('d017a028.cnv',cols = (3,2), delimiter=' ', linestyle='None', marker ='.', color ='y',checkrows = 0, newfig=False)
plt.plotfile('d017a029.cnv',cols = (3,2), delimiter=' ', linestyle='None', marker ='.', color ='r',checkrows = 0, newfig=False)
plt.plotfile('d017a030.cnv',cols = (3,2), delimiter=' ', linestyle='None', marker ='.', color ='m',checkrows = 0, newfig=False)
plt.plotfile('d017a031.cnv',cols = (3,2), delimiter=' ', linestyle='None', marker ='.', color ='c',checkrows = 0, newfig=False)
plt.xlabel('Temperature [$^\circ$C]')
plt.ylabel("Pressure [db]")
plt.title("Temperature, Cruise Hudson2014017, July 2014")
plt.legend(['cast 25','cast 26','cast 27','cast 28','cast 29','cast 30','cast 31'], loc=3,ncol=1)
plt.savefig('CTD-T.png')
plt.show()

plt.plotfile('d017a025.cnv',cols = (16,2), delimiter=' ', linestyle='None',marker ='.', color ='b',checkrows = 0)
plt.gca().invert_yaxis()
plt.plotfile('d017a026.cnv',cols = (16,2), delimiter=' ', linestyle='None', marker ='.', color ='k',checkrows = 0, newfig=False)
plt.plotfile('d017a027.cnv',cols = (16,2), delimiter=' ', linestyle='None', marker ='.', color ='g',checkrows = 0, newfig=False)
plt.plotfile('d017a028.cnv',cols = (16,2), delimiter=' ', linestyle='None', marker ='.', color ='y',checkrows = 0, newfig=False)
plt.plotfile('d017a029.cnv',cols = (16,2), delimiter=' ', linestyle='None', marker ='.', color ='r',checkrows = 0, newfig=False)
plt.plotfile('d017a030.cnv',cols = (16,2), delimiter=' ', linestyle='None', marker ='.', color ='m',checkrows = 0, newfig=False)
plt.plotfile('d017a031.cnv',cols = (16,2), delimiter=' ', linestyle='None', marker ='.', color ='c',checkrows = 0, newfig=False)
plt.xlabel('Salinity [PSU]')
plt.ylabel("Pressure [db]")
plt.title("Salinity, Cruise Hudson2014017, July 2014")
plt.legend(['cast 25','cast 26','cast 27','cast 28','cast 29','cast 30','cast 31'], loc=3,ncol=1)
plt.savefig('CTD-S.png')
plt.show()

plt.plotfile('d017a025.cnv',cols = (20,2), delimiter=' ', linestyle='None',marker ='.', color ='b',checkrows = 0)
plt.gca().invert_yaxis()
plt.plotfile('d017a026.cnv',cols = (20,2), delimiter=' ', linestyle='None', marker ='.', color ='k',checkrows = 0, newfig=False)
plt.plotfile('d017a027.cnv',cols = (20,2), delimiter=' ', linestyle='None', marker ='.', color ='g',checkrows = 0, newfig=False)
plt.plotfile('d017a028.cnv',cols = (20,2), delimiter=' ', linestyle='None', marker ='.', color ='y',checkrows = 0, newfig=False)
plt.plotfile('d017a029.cnv',cols = (20,2), delimiter=' ', linestyle='None', marker ='.', color ='r',checkrows = 0, newfig=False)
plt.plotfile('d017a030.cnv',cols = (20,2), delimiter=' ', linestyle='None', marker ='.', color ='m',checkrows = 0, newfig=False)
plt.plotfile('d017a031.cnv',cols = (20,2), delimiter=' ', linestyle='None', marker ='.', color ='c',checkrows = 0, newfig=False)
plt.xlabel('Density [sigma-theta, Kg/m^3]')
plt.ylabel("Pressure [db]")
plt.title("Density, Cruise Hudson2014017, July 2014")
plt.legend(['cast 25','cast 26','cast 27','cast 28','cast 29','cast 30','cast 31'], loc=3,ncol=1)
plt.savefig('CTD-D.png')
plt.show()
import netCDF4
from google.colab import files
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

files.upload()

nc = netCDF4.Dataset('ca_subCA_das_2020010103.nc') #Change to match dataset name

print(nc.variables.keys())

#Store variables from nc file locally
longitude = nc.variables['lon']
latitude = nc.variables['lat']
depth = nc.variables['depth']
u = nc.variables['u']
v = nc.variables['v']
time = nc.variables['time']


#Working at the depth indexed at position 8
depths = depth[8]
print(depths)


#Sets size for for the empty veloU and veloV
m,n = 25,25

#Makes the longitute and latitude the same size must be one greater then m,n
for i in range(0,m+1):
  lon = longitude[:i]
  lat = latitude[:i]

#Initializes veloU and veloV with zeros
veloU = np.zeros([m,n])
veloV = np.zeros([m,n])

figs = plt.figure(figsize = (25, 15))
axs = figs.gca()


for i in range(0,m):
  for j in range(0,n):

    veloU[i][j] = u[0][8][i][j]
    veloV[i][j] = v[0][8][i][j]

axs.quiver(lon,lat,veloU,veloV)
axs.set_xlabel('Longitude (degrees)')
axs.set_ylabel('Latitude (degrees)')
axs.set_title('Ocean Current at depth')
figs.savefig('2DOceanCurrentDirection.jpg')



# coding: utf-8

# In[100]:


import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from pyhdf.SD import SD, SDC


# In[101]:


# Open file.
FILE_NAME = 'MOD11C3.A2018244.006.2018278151628.hdf'
hdf = SD(FILE_NAME, SDC.READ)
dic = hdf.datasets()
#print(dic)
print(dic.keys())


# In[109]:


from pyhdf import SD
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import LinearSegmentedColormap
hdf = SD.SD('MOD11C3.A2018244.006.2018278151628 (1).hdf')
data = hdf.select('LST_Day_CMG')
temp=np.array(data[:,:],np.float)
temp[np.where(temp==0)]=np.nan

temp = temp *0.02 - 273.15
temp[np.where(temp<3.6)]=np.nan
temp[np.where(temp>40.6)]=np.nan

plt.figure(figsize=(20,20))
m = Basemap(projection='cyl', resolution = 'l',
    llcrnrlat=-90, urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180)


m.drawcoastlines(linewidth=0.5)
cs = m.imshow(np.flipud(temp),cmap="jet")
cbar = m.colorbar(cs,location="right")
plt.show()


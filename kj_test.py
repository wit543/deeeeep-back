
from keras.models import load_model
model = load_model('rain1.model')

import numpy as np
a = np.array([[[2.1,2,1,5,5]]])
t = model.predict(a)
print(t)


import pylab as pl
import math

file_09 = open("predict_009.csv","w")
for  i  in range(1,32):
   for h in range(0,24):
       for lat in pl.frange(6.362634,20.677349,0.001):
           for long in pl.frange(96.986175,106.082855,0.001):
               res = np.array([[[9,i,h,lat,long]]])
               print(res)
               res_a = model.predict(res)
               print("2017-09-"+'{:02d}'.format(i)+" "+'{:02d}'.format(h)+":00:00,"+'{:6f}'.format(lat)+","+'{:6f}'.format(long))
               res_b = abs(res_a[0][0])
               res_c = '{:0.1f}'.format(res_b)
               print(res_c)
               file_09.write("2017-09-"+'{:02d}'.format(i)+" "+'{:02d}'.format(h)+":00:00,"+'{:6f}'.format(lat)+","+'{:6f}'.format(long)+","+res_c+"\n")


file_10 = open("predict_010.csv","w")
for  i  in range(1,31):
   for h in range(0,24):
       for lat in pl.frange(6.362634,20.677349,0.001):
           for long in pl.frange(96.986175,106.082855,0.001):
               res = np.array([[[10,i,h,lat,long]]])
               res_a = model.predict(res)
               print("2017-10-"+'{:02d}'.format(i)+" "+'{:02d}'.format(h)+":00:00,"+'{:6f}'.format(lat)+","+'{:6f}'.format(long))
               res_b = abs(res_a[0][0])
               res_c = '{:0.1f}'.format(res_b)
               print(res_c)
               file_10.write("2017-10-"+'{:02d}'.format(i)+" "+'{:02d}'.format(h)+":00:00,"+'{:6f}'.format(lat)+","+'{:6f}'.format(long)+","+res_c+"\n")
import matplotlib.pyplot as plt
import numpy as np
import time


fig=plt.figure()
plt.axis([-1, 1, -1, 1])

i=0
y=list()
x=list()
#Hit count and Miss count for points inside/outside of circle respectively
hit=1
miss=1

plt.ion()
plt.show()

while i < 100:

  temp_y=np.random.random()*2. - 1.
  temp_x=np.random.random()*2. - 1.
#Increase Count of miss if outside circle of radius 1
  if np.sqrt(temp_y**2. + temp_x**2.) > 1.: #Total distance to point
    plt.scatter(temp_x, temp_y, color='b')
    miss+=1
#Increase Count of hit if inside circle
  else:
    plt.scatter(temp_x, temp_y, color='r')
    hit+=1
  i+=1
  plt.draw()
  print(float(hit)/float(hit+miss)) * 4.

i=0

hit = 1
miss = 1

#Same as above but without plotting
while i < 1000000:
  temp_y=np.random.random()*2. - 1.
  temp_x=np.random.random()*2. - 1.

  if np.sqrt(temp_y**2. + temp_x**2.) > 1.:
    miss+=1
  else:
    hit+=1
  i+=1
print("=========")
print("=========")
print(float(hit)/float(hit+miss)) * 4.

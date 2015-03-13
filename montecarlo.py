import matplotlib.pyplot as plt
import numpy as np
import time

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

#Author: Vignesh Sathyaseelan
#Email: vsathyas@purdue.edu

import numpy as np,copy,os,time
import matplotlib.pyplot as plt

def fd_grad(x,func,h=0.01):
    #this function returns the energy and force on a particle (Force calculated using central difference formula)
    grad = -1*np.array([(func([x[0]+h,x[1]])-func([x[0]-h,x[1]]))/2*h,\
         (func([x[0],x[1]+h])-func([x[0],x[1]-h]))/2*h])
    return grad
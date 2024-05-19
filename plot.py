#Author: Vignesh Sathyaseelan
#Email: vsathyas@purdue.edu

import numpy as np,copy,os,time
import matplotlib.pyplot as plt

def plot_PES(potential,xmin,xmax,positions,initial_position,spacing=0.1,outname='out',savefig=True):
    
    plt.figure(figsize=(5,5))
    plt.xlim(-xmax,xmax)
    plt.ylim(-xmax,xmax)
    grid_x,grid_y = np.meshgrid(np.arange(-xmax,xmax,spacing), np.arange(-xmax,xmax,spacing))
    plt.contourf(grid_x, grid_y, potential([grid_x,grid_y]))
    plt.scatter(positions[:,0],positions[:,1],color='grey',s=50)
    plt.scatter(initial_position[0],initial_position[1],color='black',label='Start',edgecolor='black',s=50)
    plt.scatter(positions[-1,0],positions[-1,1],color='red',label='End',edgecolor='black',s=50)
    plt.legend()
    if savefig: plt.savefig(f'{outname}.png')

    return

def plot_temp(times,temperature,outname='temp',savefig=True):
    
    plt.figure(figsize=(5,5))
    plt.plot(times,temperature,alpha=0.5)
    plt.title('Annealing Profile')
    plt.ylabel('Temperature')
    plt.xlabel('Iteration')
    if savefig: plt.savefig(f'{outname}.png')

    return

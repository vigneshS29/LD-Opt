#Author: Vignesh Sathyaseelan
#Email: vsathyas@purdue.edu

import numpy as np,copy,os,time
import matplotlib.pyplot as plt

from sald import *
from grad import *
from plot import *

def main(): 
    
    potential = lambda x: (x[0]**2 + x[1]**2)
    initial_position=[5,5]

    st = time.time()

    steps,positions,temperature = sald(potential=potential,initial_position=initial_position,gamma=1,alpha=0.99\
                                    ,T=10**5,max_anneal_cycle=100,max_time=5000,dt=0.1,save_frequency=10)

    print(f'Finished in {np.round(time.time()-st,2)} seconds')
    
    plot_PES(potential=potential,initial_position=initial_position,xmin=-10,xmax=10,positions=positions)
    plot_temp(steps,temperature)

    return

if __name__ == '__main__':
    main()

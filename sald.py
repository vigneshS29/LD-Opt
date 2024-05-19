#Author: Vignesh Sathyaseelan
#Email: vsathyas@purdue.edu

import numpy as np,copy,os,time
import matplotlib.pyplot as plt

from grad import *

#this is step A
def position_update(x,v,dt):
    x_new = x + v*dt/2.
    return x_new

#this is step B
def velocity_update(v,F,dt):
    v_new = v + F*dt/2.
    return v_new

def random_velocity_update(v,gamma,T,dt):

    kB = 1.380649 * (10**-23)
    R = np.random.normal()
    c1 = np.exp(-gamma*dt)
    c2 = np.sqrt(1-c1**2)*np.sqrt(kB*T)
    v_new = c1*v + R*c2
    return v_new

def sald(potential, gamma, alpha, initial_position=None, initial_velocity=None, T=3*(10**25),max_anneal_cycle=100 ,max_time=10**3, dt = 10**-2, save_frequency=10):

    #set initial parameters and variables
    initial_temp = T
    anneal_step = 0
    step_number = 0
    step_numbers = []
    positions = []
    temperature = []
    initial_position = initial_position

    print(f'Running SALD-OPT with initial_point = {initial_position} and intitial temp {T} for {max_anneal_cycle} anneal cycles and each cycle for {max_time}')
    while anneal_step <= max_anneal_cycle:
        
        #set initial parameters for each anneal cycle
        t = 0

        #Temperature Anneal 
        if anneal_step%5 == 0: 
            T = initial_temp
            initial_temp *= alpha

        print(f'Running anneal cycle {anneal_step} with temperature {T}')

        try: os.remove(f'out_{anneal_step}.txt')
        except: pass

        with open(f'out_{anneal_step}.txt','a') as f:
            f.write('time\tTemperature\tX\tY\tVelocity\n')

        if anneal_step == 0 and initial_position == None: x = np.random.normal(10,size=2)
        else: x = initial_position

        if initial_velocity: v = initial_velocity
        else: v = np.random.normal(size=2)

        while t<max_time:

            #Temperature Anneal
            if step_number%10000==0: 
                #T = T*(np.exp(-((alpha*10)*time)))
                T = T*alpha
      
            # B
            potential_energy, force = potential(x),fd_grad(x,potential)
            v = velocity_update(v,force,dt)
            
            #A
            x = position_update(x,v,dt)

            #O
            v = random_velocity_update(v,gamma,T,dt)
            
            #A
            x = position_update(x,v,dt)
            
            # B
            potential_energy, force = potential(x),fd_grad(x,potential)
            v = velocity_update(v,force,dt)

            if step_number%save_frequency == 0:
                step_numbers += [step_number]
                positions += [x]
                temperature += [T]
                
                with open(f'out_{anneal_step}.txt','a') as f:
                    f.write(f'{t:.3f}\t{T:.3}\t{x[0]:.3f}\t{x[1]:.3f}\t{str(np.round(v,5))}\n')
            
            t += dt
            step_number += 1
        
        print(f'Anneal step {anneal_step} done. Optimized to = {x}')
        initial_position = x
        anneal_step += 1
        
    return step_numbers, positions, temperature

import numpy as np 
#import matplotlib.pyplot as plt

cdef double heat_solver(h,k,init='sine'):
    '''solve the heat equation using with space step h and time step k along the interval [0,1]'''
    cdef int i, j
    u = np.zeros((2,1/h+1))
    gamma = k/h**2
    x = np.linspace(0,1,num=1/h+1)
    if init == 'sine': 
        u[1,:] = np.sin(pi*x)
    if init == 'arc':
        u[1,:] = x*(1-x)
    for i in np.arange(0,1/k+1):
        u[0,:] = u[1,:]
        for j in np.arange(1,1/h): 
            u[1,j] = u[0,j] + gamma * (u[0,j+1] - 2*u[0,j] + u[0,j-1])            
        #apply boundary conditions
        u[1,0] = 0
        u[1,-1] = 0
    return u 


#test= heat_solver(0.1,0.0001, init = 'arc') 
#plot(np.exp(-pi**2*1)*np.sin(pi*x))




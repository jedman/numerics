import numpy as np 
import math
def heat_solver(hinv,kinv,init='sine'):
    '''solve the heat equation using with space step h and time step k along the interval [0,1]'''
    cdef int i, j
    cdef double pi = math.pi
    u = np.zeros((2,hinv+1))
    gamma = (1./kinv)/(1./hinv)**2
    x = np.linspace(0,1,num=hinv+1)
    if init == 'sine': 
        u[1,:] = np.sin(pi*x)
    if init == 'arc':
        u[1,:] = x*(1-x)
    for i in xrange(0,kinv):
        u[0,:] = u[1,:]
        for j in xrange(1,hinv): 
            u[1,j] = u[0,j] + gamma * (u[0,j+1] - 2*u[0,j] + u[0,j-1])            
        #apply boundary conditions
        u[1,0] = 0
        u[1,-1] = 0 
    return u 
def heat_solver_full(hinv,kinv,init='sine'):
    '''solve the heat equation using with space step 1/hinv and time step 1/kinv along the interval [0,1]
    and return the entire result'''
    cdef int i, j
    cdef double pi = math.pi
    u = np.zeros((kinv+1,hinv+1))
    gamma = (1./kinv)/(1./hinv)**2
    x = np.linspace(0,1,num=hinv+1)
    if init == 'sine': 
        u[0,:] = np.sin(pi*x) 
    if init == 'arc':
        u[0,:] = x*(1-x)
    for i in xrange(0,kinv):
        #u[i,:] = u[i+1,:]
        for j in xrange(1,hinv): 
            u[i+1,j] = u[i,j] + gamma * (u[i,j+1] - 2*u[i,j] + u[i,j-1])            
        #apply boundary conditions
        u[i+1,0] = 0
        u[i+1,-1] = 0 
    return u





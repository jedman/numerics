import heat_solver
import matplotlib.pyplot as plt 
import numpy as np 
from scipy import interpolate

### gamma = 1/6 mesh refinement 
hinv = 10 
kinv = 600 
time600 = np.linspace(0,1,num=kinv+1) 
u_600 = heat_solver.heat_solver(hinv,kinv) 
gamma = hinv**2./kinv
print gamma 

hinv = 20
kinv = 2400
time2400 = np.linspace(0,1,num=kinv+1) 
u_2400 = heat_solver.heat_solver(hinv,kinv) 
gamma = hinv**2./kinv
print gamma 

hinv = 40
kinv = 9600
time9600 = np.linspace(0,1,num=kinv+1) 
u_9600 = heat_solver.heat_solver(hinv,kinv) 
gamma = hinv**2./kinv
print gamma 

x = np.linspace(0,1,num=11) 
x21 = np.linspace(0,1,num = 21) 
u_24 = interpolate.interp1d(x21,u_2400[1,:])
x41 = np.linspace(0,1,num=41) 
u_96 = interpolate.interp1d(x41,u_9600[1,:])

p_space = np.log((u_600[1,:]-u_24(x))/(u_24(x)-u_96(x)))/np.log(2.) 
print 'spatial convergence order for lambda = 1/6 is ', p_space[1] 
p_time = np.log((u_600[1,:]-u_24(x))/(u_24(x)-u_96(x)))/np.log(4.) 
print 'temporal convergence order for lambda = 1/6 is ', p_time[1] 


fig1 = plt.figure() 
ax1 = fig1.add_subplot(111)
ax1.plot(x,u_600[1,:], label = 'h=1/10') 
ax1.plot(x21,u_2400[1,:], label = 'h=1/20') 
ax1.plot(x41,u_9600[1,:], label ='h=1/40')
ax1.set_title('u at t=1 with $\lambda =1/6$')
ax1.set_xlabel('x')
ax1.set_ylabel('u')
ax1.legend()
plt.savefig('u1_6_conv.pdf', bbox_inches=0)

### gamma = 1/2 mesh refinement

time200 = np.linspace(0,1,num=kinv+1) 
hinv = 10 
kinv = 200 
u_200 = heat_solver.heat_solver(hinv,kinv) 
gamma = hinv**2./kinv
print gamma 

hinv = 20
kinv = 800
time800 = np.linspace(0,1,num=kinv+1) 
u_800 = heat_solver.heat_solver(hinv,kinv) 
gamma = hinv**2./kinv
print gamma 

hinv = 40
kinv = 3200
time3200 = np.linspace(0,1,num=kinv+1) 
u_3200 = heat_solver.heat_solver(hinv,kinv) 
gamma = hinv**2./kinv
print gamma 

x21 = np.linspace(0,1,num = 21) 
u_80 = interpolate.interp1d(x21,u_800[1,:])
x41 = np.linspace(0,1,num=41) 
u_320 = interpolate.interp1d(x41,u_3200[1,:])

fig2 = plt.figure() 
ax2 = fig2.add_subplot(111)
ax2.plot(x,u_200[1,:], label = 'h=1/10') 
ax2.plot(x21,u_800[1,:], label = 'h=1/20') 
ax2.plot(x41,u_3200[1,:], label ='h=1/40')
ax2.set_title('u at t=1 with $\lambda =1/2$')
ax2.set_xlabel('x')
ax2.set_ylabel('u')
ax2.legend() 
plt.savefig('u1_2_conv.pdf', bbox_inches=0)

p_space = np.log((u_200[1,:]-u_80(x))/(u_80(x)-u_320(x)))/np.log(2.) 
print 'spatial convergence order for lambda = 1/2 is ', p_space[1] 
p_space = np.log((u_200[1,:]-u_80(x))/(u_80(x)-u_320(x)))/np.log(4.) 
print 'temporal convergence order for lambda = 1/2 is ', p_time[1]


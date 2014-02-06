import numpy as np
import matplotlib.pyplot as plt 
from scipy import interpolate
import pyximport
pyximport.install()
import heat_solver 

def coeff(x):
	alpha = np.exp(x)
	return alpha 

alpha2 = lambda x: np.exp(2*x)

hinv = 10 
kinv = 600 
time600 = np.linspace(0,1,num=kinv+1)
x = np.linspace(0,1,num = hinv+1 )
alpha = coeff(x)
#alpha = alpha[::-1] #reverse alpha
u_600 = heat_solver.heat_solver_nl(hinv,kinv, alpha) 

hinv = 20
kinv = 2400
x = np.linspace(0,1,num = hinv+1 )
time2400 = np.linspace(0,1,num=kinv+1) 
alpha = coeff(x)
#alpha = alpha[::-1] #reverse alpha
u_2400 = heat_solver.heat_solver_nl(hinv,kinv, alpha) 

hinv = 40
kinv = 9600
x = np.linspace(0,1,num = hinv+1 )
alpha = coeff(x)
#alpha = alpha[::-1] #reverse alpha
time9600 = np.linspace(0,1,num=kinv+1) 
u_9600 = heat_solver.heat_solver_nl(hinv,kinv, alpha) 

x = np.linspace(0,1,num=11) 
x21 = np.linspace(0,1,num = 21) 
u_24 = interpolate.interp1d(x21,u_2400[1,:])
x41 = np.linspace(0,1,num=41) 
u_96 = interpolate.interp1d(x41,u_9600[1,:])

fig1 = plt.figure() 
ax1 = fig1.add_subplot(111)
ax1.plot(x,u_600[1,:], label = 'h=1/10') 
ax1.plot(x21,u_2400[1,:], label = 'h=1/20') 
ax1.plot(x41,u_9600[1,:], label ='h=1/40')
ax1.set_title('u at t=1 with $\\alpha =e^{2x}$')
ax1.set_xlabel('x')
ax1.set_ylabel('u')
ax1.legend()
plt.savefig('unl_conv.pdf', bbox_inches=0)

p_space = np.log((u_600[1,1:10]-u_24(x[1:10]))/(u_24(x[1:10])-u_96(x[1:10])))/np.log(2.) 
#print 'spatial convergence order for lambda = 1/6 is ', p_space 
p_time = np.log((u_600[1,1:10]-u_24(x[1:10]))/(u_24(x[1:10])-u_96(x[1:10])))/np.log(4.) 
#print 'temporal convergence order for lambda = 1/6 is ', p_time 

f3, ((ax3,ax4,ax5)) = plt.subplots(3, sharex=True)
ax3.plot(x[1:10],p_space, label = 'space') 
ax4.plot(x[1:10],p_time, label = 'time') 
ax3.set_title('order of convergence for  $ \\alpha =e^{2x}$')
ax3.set_ylabel('p')
ax4.set_ylabel('p')
ax3.legend()
ax4.legend()

ax5.plot(x,1./6*alpha2(x), label='$\\alpha\lambda$') 
ax5.set_title('$\\alpha\lambda$ for constant k nonlinear case, $\\alpha = e^{2x}$')
ax5.set_xlabel('x')
ax5.set_ylabel('$\\alpha\lambda$')
ax5.legend()
plt.savefig('unl_orderconv.pdf', bbox_inches=0)




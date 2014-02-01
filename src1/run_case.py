import heat_solver 
import matplotlib.pyplot as plt 
import numpy as np 
u1 = heat_solver.heat_solver(0.1,0.1) 
u2 = heat_solver.heat_solver(0.1,0.005)
u3 = heat_solver.heat_solver(0.1,1./600)
u1_arc = heat_solver.heat_solver(0.1,1./600, init ='arc') 

x = np.linspace(0,1,num=11)
fig1 = plt.figure() 
ax1 = fig1.add_subplot(111)
ax1.plot(x,u1[1,:]) 
plt.savefig('u1.png', bbox_inches=0)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)  
ax2.plot(x,u2[1,:])
plt.savefig('u2.png', bbox_inches=0)
plt.show()

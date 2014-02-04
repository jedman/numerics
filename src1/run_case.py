import heat_solver 
import matplotlib.pyplot as plt 
import numpy as np 
u1 = heat_solver.heat_solver(10,10) 
u2 = heat_solver.heat_solver(10,200)
u3 = heat_solver.heat_solver(10,600)
u4 = heat_solver.heat_solver(10,2000)
#u1_arc = heat_solver.heat_solver(10,600, init ='arc') 
#u_full = heat_solver.heat_solver_full(10,200)

x = np.linspace(0,1,num=11)
fig1 = plt.figure() 
ax1 = fig1.add_subplot(111)
ax1.plot(x,u1[1,:]) 
ax1.set_title('u at t=1 with $\lambda =10$')
ax1.set_xlabel('x')
ax1.set_ylabel('u')
plt.savefig('u1.pdf', bbox_inches=0)


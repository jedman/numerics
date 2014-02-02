import heat_solver 
import matplotlib.pyplot as plt 
import numpy as np 
u1 = heat_solver.heat_solver(10,10) 
u2 = heat_solver.heat_solver(10,200)
u3 = heat_solver.heat_solver(10,600)
u1_arc = heat_solver.heat_solver(10,600, init ='arc') 
u_full = heat_solver.heat_solver_full(10,200)



x = np.linspace(0,1,num=11)
fig1 = plt.figure() 
ax1 = fig1.add_subplot(111)
ax1.plot(x,u1[1,:]) 
plt.savefig('u1.png', bbox_inches=0)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)  
ax2.plot(x,u2[1,:])
plt.savefig('u2.png', bbox_inches=0)
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)  
ax3.plot(x,u_full[200,:])
plt.show()

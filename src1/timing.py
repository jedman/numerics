import pstats, cProfile
import numpy as np
import matplotlib.pyplot as plt 
import pyximport
pyximport.install()
import heat_solver 


hinv =10 
kinv = 600
x =np.linspace(0,1,num = hinv+1)

u_sine = heat_solver.heat_solver(hinv,kinv) 
u_sine_200 = heat_solver.heat_solver(hinv, 200) 
u_arc = heat_solver.heat_solver(hinv,kinv, init ='arc')
u_arc_200 = heat_solver.heat_solver(hinv,200, init ='arc')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)  
ax2.plot(x,u_sine[1,:], label = 'numerical, $\lambda=1/6$', ls ='--', marker = 'o')
ax2.plot(x,heat_solver.exact(x,1), label = 'exact')
ax2.plot(x,u_sine_200[1,:], label = 'numerical, $\lambda=1/2$', ls ='--', marker ='x')
ax2.set_title('Exact and numerical solutions at t=1 with I.C. $\sin(\pi x)$ ')
ax2.set_xlabel('x')
ax2.set_ylabel('u')
ax2.legend()
plt.savefig('u_sine.pdf', bbox_inches=0)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)  
ax2.plot(x,u_arc[1,:], label = 'numerical,$\lambda=1/6$', ls ='--', marker ='o')
ax2.plot(x,heat_solver.exact(x,2, init='arc'), label = 'exact')
ax2.plot(x,u_arc_200[1,:], label = 'numerical, $\lambda=1/2$', ls ='--', marker ='x')
ax2.set_title('Exact and numerical solutions at t=1 with I.C. $x(1-x)$ ')
ax2.set_xlabel('x')
ax2.set_ylabel('u')
ax2.legend()
plt.savefig('u_arc.pdf', bbox_inches=0)

cProfile.runctx("heat_solver.heat_solver(hinv, kinv)",globals(), locals(), "heatsolver_sine.prof")
s = pstats.Stats("heatsolver_sine.prof") 
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("heat_solver.heat_solver(hinv, 200)",globals(), locals(), "heatsolver_sine_coarse.prof")
s = pstats.Stats("heatsolver_sine_coarse.prof") 
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("heat_solver.exact(x, 1, init = 'arc')",globals(), locals(), "exact_sine.prof")
s = pstats.Stats("exact_sine.prof") 
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("heat_solver.heat_solver(hinv, kinv, init='arc')",globals(), locals(), "heatsolver_arc.prof")
s = pstats.Stats("heatsolver_arc.prof") 
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("heat_solver.heat_solver(hinv, 200, init='arc')",globals(), locals(), "heatsolver_arc_coarse.prof")
s = pstats.Stats("heatsolver_arc_coarse.prof") 
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("heat_solver.exact(x, 1, init = 'arc')",globals(), locals(), "exact_arc3.prof")
s = pstats.Stats("exact_arc3.prof") 
s.strip_dirs().sort_stats("time").print_stats()

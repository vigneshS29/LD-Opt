# SALD-Opt: A Combined Langevin dynamics &amp; Simulated Annealing based optimization algorithm.

Deep learning require global optimization of non-convex objective functions with multiple local minima. Langevin Dynamics (LD) with Simulated Annealing (SA) is a approach used in physical simulation for minimization of many-particle potentials. In this package SA & LD are leveraged for the optimization of non-convex objectice function.

Results of a optimization run on the rastrigin function $$ ({x}_{i}^2 - cos(2\pi) {x}_{i}) )+ ({x}_{j}^2 - cos(2\pi {x}_{j})) $$ :

![](out.png)

Temperature annel curve:

![](temp.png)

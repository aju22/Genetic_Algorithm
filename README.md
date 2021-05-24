# Introduction
This is a simple, yet a powerful visualisation of Genetic Algorithm, that literally uses "Survival of Fittest" to optimally reach a target.

In this case, we start with a bunch of rockets who have no idea what's going on.

In further generations, we can see them trying to seek a particular target, even when obstacles are placed.

After enough generations, they behave ideally/optimally and sucessfully reach the target.

# Genetic Algorithms
Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection. It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve. It is frequently used to solve optimization problems, in research, and in machine learning.

In GAs, we have a pool or a population of possible solutions to the given problem. These solutions then undergo recombination and mutation (like in natural genetics), producing new children, and the process is repeated over various generations. Each individual (or candidate solution) is assigned a fitness value (based on its objective function value) and the fitter individuals are given a higher chance to mate and yield more “fitter” individuals. This is in line with the Darwinian Theory of “Survival of the Fittest”.

In this way we keep “evolving” better individuals or solutions over generations, till we reach a stopping criterion.

Genetic Algorithms are sufficiently randomized in nature, but they perform much better than random local search (in which we just try various random solutions, keeping track of the best so far), as they exploit historical information as well.


# Generation 1
Well, this is just an absolute mess !

![gen1](Resources/gen1.gif)
# Generation 4
Okay, Baby steps.

![gen1](Resources/gen4.gif)
# Generation 10 
Pretty Good.

![gen1](Resources/gen10.gif)

# Code Used
  
  Python.
  
  p5 library.

# Resources
 
 https://en.wikipedia.org/wiki/Genetic_algorithm

 https://natureofcode.com/book/chapter-9-the-evolution-of-code/
 
 https://www.youtube.com/watch?v=RxTfc4JLYKs

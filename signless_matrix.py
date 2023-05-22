#!/usr/bin/env sage -python

from sage.all import *
from functions import laplacian_energy
import time

start = time.time()

# Generating graphs using Nauty
n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
nauty_list = list(graphs.nauty_geng(parameters))

matrices = [graph.kirchhoff_matrix(signless=True) for graph in nauty_list]
energy = [laplacian_energy(matrix.eigenvalues(), n, m) for matrix in matrices]
index = energy.index(min(energy))

finish = time.time()

# Saving the graph plot as a PNG file
filename = "graph_" + str(n) + ".png"
nauty_list[index].plot().save(filename)

print(f"Min. signless L. energy: {round(min(energy), 5)}")
print(f"Execution time: {round(finish - start, 2)} s")

#!/usr/bin/env sage -python

from sage.all import *
from functions import laplacian_energy
import time

start = time.time()

# Generating graphs using Nauty
n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
graphs_nauty = list(graphs.nauty_geng(parameters))

energy = [laplacian_energy(graph.spectrum(laplacian=True), n, m) for graph in graphs_nauty]
index = energy.index(min(energy))

finish = time.time()

# Saving the graph plot as a PNG file
filename = "graph_" + str(n) + ".png"
graphs_nauty[index].plot().save(filename)

print(f"Minimum Laplacian energy: {round(min(energy), 5)}")
print(f"Execution time: {round(finish - start, 2)} s")

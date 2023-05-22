#!/usr/bin/env sage -python

from sage.all import *
from functions import laplacian_energy
import time

start = time.time()

# Generating graphs using Nauty
n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
nauty_list = list(graphs.nauty_geng(parameters))

energy = [laplacian_energy(graph.spectrum(laplacian=True), n, m) for graph in nauty_list]
index = energy.index(min(energy))

# Saving the graph plot as a PNG file
filename_1 = "graph_" + str(n) + "_1st.png"
nauty_list[index].plot().save(filename_1)
print(f"Minimum Laplacian energy: {round(min(energy), 5)}")

# Deleting first index and calculating new energy
del energy[index]
new_index = energy.index(min(energy))

# Saving the graph plot as a PNG file
filename_2 = "graph_" + str(n) + "_2nd.png"
nauty_list[new_index].plot().save(filename_2)
print(f"Second minimum Laplacian energy: {round(min(energy), 5)}")

finish = time.time()

print(f"Execution time: {round(finish - start, 2)} s")

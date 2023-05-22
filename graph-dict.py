#!/usr/bin/env sage -python

from sage.all import *
from functions import laplacian_energy as le
import time

start = time.time()

# Generating graphs using Nauty
n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
nauty_list = list(graphs.nauty_geng(parameters))
print(f"Graphs generated: {len(nauty_list)}")

# Adding indexes and graphs to dictionary
nauty_dict = dict()
for index, graph in enumerate(nauty_list):
    nauty_dict[index] = graph

# Calculating the Laplacian energy and setting an index for the first graph
energy = laplacian_energy(nauty_list[0].spectrum(laplacian=True), n, m)
index = 0

for index, graph in nauty_dict.items():
    new_energy = laplacian_energy(graph.spectrum(laplacian=True), n, m)
    new_index = index
    if new_energy < energy:
        energy = new_energy
        index = new_index
        print(f"Partial min. L. energy: {round(energy, 5)} - Graph: {index}")

finish = time.time()

# Saving the graph plot as a PNG file
filename = "graph_" + str(n) + ".png"
nauty_list[index].plot().save(filename)

print(f"Minimum Laplacian energy: {round(energy, 5)}")
print(f"Execution time: {round(finish - start, 2)} s")

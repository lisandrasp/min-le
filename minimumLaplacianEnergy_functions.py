#!/usr/bin/env sage -python

from sage.all import *
from functions import *
import time
import os

time_start = time.time()

# Generating graphs using Nauty
n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
nauty_list = list(graphs.nauty_geng(parameters))
# Graphs will be evaluated in groups of 240 per cycle
print(f"Graphs generated: {len(nauty_list)}\nCycles: {len(nauty_list) // 240 + 1}")

# Adding indexes and graphs to a list then to a tuple
nauty_list_indexed = list()
for index, graph in enumerate(nauty_list):
    nauty_list_indexed.append((index, graph))
nauty_tuple = tuple(nauty_list_indexed)

# Calculating the Laplacian energy and setting an index for the first graph
energy = laplacian_energy(nauty_list[0].spectrum(laplacian=True), n, m)
index = 0

spectrum = list()
graph_tuple = tuple()

# Setting parameters for iteration
cycle = 0
start = 0
finish = 240

while finish - 240 <= len(nauty_tuple) + 1:
    for new_graph_tuple in nauty_tuple[start:finish]:
        new_spectrum = new_graph_tuple[1].spectrum(laplacian=True)
        new_energy = laplacian_energy(new_spectrum, n, m)
        new_index = new_graph_tuple[0]
        if new_energy < energy:
            spectrum = new_spectrum
            energy = new_energy
            graph_tuple = new_graph_tuple[1]
            index = new_index
            # Saving the partial result's graph plot as a PNG file
            nauty_list[index].plot().save(str("graph_partial_" + str(n) + ".png"))
            # Saving the energy value as a text file
            with open("energy.txt", "w") as graph_energy:
                graph_energy.write(str(round(energy, 5)))
    start += 240
    finish += 240
    cycle += 1
    print(f"Cycle: {cycle} - Partial min. L. energy: {round(energy, 5)} - Graph: {index}")

time_finish = time.time()

# Saving the graph plot as a PNG file
filename = "graph_" + str(n) + ".png"
nauty_list[index].plot().save(filename)
# Removing the partial result's PNG file
if os.path.exists(str("graph_" + str(n) + ".png")):
    os.remove(str("graph_partial_" + str(n) + ".png"))

print(f"Minimum Laplacian energy: {round(energy, 5)}")
print(f"Sigma: {sigma(graph_tuple, spectrum)}")
print(f"Diameter: {diameter(graph_tuple)}")
print(f"Execution time: {round(time_finish - time_start, 2)} s")
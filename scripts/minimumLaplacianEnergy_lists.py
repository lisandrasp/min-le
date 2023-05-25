#!/usr/bin/env sage -python

from sage.all import *
from functions import laplacian_energy
import time

start = time.time()

# Generating graphs using Nauty
n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
nauty_list = list(graphs.nauty_geng(parameters))

# Separating graphs in lists
size = 240
graph_lists = [nauty_list[i:i + n] for i in range(0, len(nauty_list), size)]

spectrum_all = list()
for graph_list in graph_lists:
    spectrum_list = [list_1.spectrum(laplacian=True) for list_1 in graph_list]
    spectrum_all.append(spectrum_list)

spectrum_join = list()
for list_2 in spectrum_all:
    spectrum_join += list_2

energy = [laplacian_energy(list_3, n, m) for list_3 in spectrum_join]
index = energy.index(min(energy))

finish = time.time()

# Saving the graph plot as a PNG file
filename = "graph_" + str(n) + ".png"
nauty_list[index].plot().save(filename)

print(f"Minimum Laplacian energy: {round(min(energy), 5)}")
print(f"Execution time: {round(finish - start, 2)} s")

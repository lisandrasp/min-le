#!/usr/bin/env sage -python

import time
from sage.all import *
from functions import unicyclic_graphs
from functions import laplacian_energy as le

start = time.time()

# Set parameters
n, m = 10, 10  # Vertices and edges
lenght = 240

# Generate graphs
graphs = unicyclic_graphs(n, m)

# Split graphs in lists of defined lenght
graph_lists = [graphs[graph:graph+lenght] for graph in range(0, len(graphs), lenght)]

spectra = list()
for graph_list in graph_lists:
    # Compute spectrum of each graph in a list
    spectra_list = [graph.spectrum(laplacian=True) for graph in graph_list]
    # Store spectra lists in a list
    spectra.append(spectra_list)

# Join all spectra in a single list
spectra_all = list()
for spectrum in spectra_all:
    spectra_all += spectrum

# Compute Laplacian energy
energy = [le(spectrum, n, m) for spectrum in spectra_all]

# Find minimum Laplacian energy
minimum = min(energy)
index = energy.index(minimum)

end = time.time()

# Save graph plot as PNG file
file = f"graph-{n}.png"
graphs[index].plot().save(file)
print(f"LE min:{round((minimum), 5)\nTime: {time}")

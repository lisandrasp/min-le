#!/usr/bin/env sage -python

import time
from sage.all import *
from functions import unicyclic_graphs
from functions import laplacian_energy as le

start = time.time()

# Set parameters
n, m = 10, 10  # Vertices and edges

# Generate graphs
graphs = unicyclic_graphs(n, m) 

# Compute Laplacian energy
energy = [le(graph.spectrum(laplacian=True), n, m) for graph in graphs]

# Find minimum le
minimum = min(energy)

# Find index of minimum le 
index = energy.index(minimum)
end = time.time()
time = end-start

# Save graph plot as PNG file
file = f"graph-{n}.png"
graphs[index].plot().save(file)
print(f"LE min: {round((minimum), 5)}\nTime: {time}")

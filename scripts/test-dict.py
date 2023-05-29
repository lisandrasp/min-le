#!/usr/bin/env sage -python

from sage.all import *
from functions import unicyclic_graphs
from functions import laplacian_energy as le

# Set parameters
n, m = 10, 10  # Vertices and edges

# Generate graphs
graphs = list(unicyclic_graphs(n, m))
graphs_dict = dict()

for index, graph in enumerate(graphs):
    # Give graph a key
    graphs_dict[index] = graph

# Compute Laplacian energy for the 1st graph
energy = le(graphs[0].spectrum(laplacian=True), n, m)

# Set index for the 1st graph
index = 0

for index, graph in graphs_dict.items():
    new_energy = le(graph.spectrum(laplacian=True), n, m)
    new_index = index
    if new_energy < energy:
        energy = new_energy
        index = new_index
    print(f"LE min: {round(energy, 5)}")

# Save graph plot as PNG
file = f"{n}-min.png"
graphs[index].plot().save(file)

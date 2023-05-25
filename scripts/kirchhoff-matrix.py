#!/usr/bin/env sage -python

from sage.all import *
from functios import unicyclic_graphs
from functions import laplacian_energy as le

# Set parameters
n, m = 10, 10  # Vertices and edges

# Generate graphs
graphs = unicyclic_graphs(n, m)

# Make Kirchhoff matrices
matrices = [graph.kirchhoff_matrix(signless=True) for graph in graphs]

# Compute Laplacian energy for all graphs
energy = [le(matrix.eigenvalues(), n, m) for matrix in matrices]

# Find minimum energy
minimum = min(energy)

# Find energy index
index = energy.index(minimum)

# Save graph plot as PNG 
file = f"{n}-min.png"
graphs[index].plot().save(file)

# Show Laplacian energy
print(f"LE min: {round(minimum, 5)}")

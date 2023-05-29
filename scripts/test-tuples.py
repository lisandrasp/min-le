#!/usr/bin/env sage -python

import os
import time
from sage.all import *
from functions import unicyclic_graphs
from functions import laplacian_energy as le

time_start = time.time()

# Set parameters
n, m = 10, 10   # Vertices and edges
interval = 250  # Lap size

# Generate graphs
graphs = unicyclic_graphs(n, m)
graphs_list = list()

for index, graph in enumerate(graphs):
    # Add index to graph
    graphs_list.append((index, graph))

# Make list into tuple
graphs_tuple = tuple(graphs_list)

# Compute Laplacian energy for the 1st graph
energy = le(graphs[0].spectrum(laplacian=True), n, m)

# Set index for the 1st graph
index = 0

# Initialize variables
lap = 0
start = 0
end = interval

while end-interval <= len(graphs_tuple)+1:
    for graph in graphs_tuple[start:end]:
        new_energy = le(graph[1].spectrum(laplacian=True), n, m)
        new_index = graph[0]
        if new_energy < energy:
            energy = new_energy
            index = new_index

            # Save graph information
            graphs[index].plot().save(f"graph-{n:02}.png"))
            with open("energy.txt", "w") as file:
                file.write(energy)
    start += interval 
    finish += interval
    lap += 1
    print(f"LE min: {round(energy, 5)}")

time_end = time.time()
time = time_end-time_start

print(f"Time: {time}")

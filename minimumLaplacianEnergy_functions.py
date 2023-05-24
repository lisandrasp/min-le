#!/usr/bin/env sage -python

import os
# import time
from sage.all import *
from functions import unicyclic_graphs, sigma, diameter, save_graph, write_energy
from functions import laplacian_energy as le

# time_start = time.time()

# Set parameters
n, m = 10, 10  # Vertices and edges
interval = 250  # Set size
folder = "plots"

# Generate graphs
graphs = unicyclic_graphs(n, m)
graphs_list = list()

for index, graph in enumerate(graphs):
    # Add index to graph
    graphs_list.append((index, graph))

# Make enumerate object into tuple
graphs_tuple = tuple(graphs_index)

# Create folder to store graph plots
path = os.path.join(folder)
if not os.path.exists(path):
    os.mkdir(path)

# Write first row of energies table
write_energy("i", "n", "LE")
spectrum = list()
graph_tuple = tuple()

# Compute Laplacian energy for the 1st graph
energy = le(graphs[0].spectrum(laplacian=True), n, m)
# Set index for the 1st graph
index = 0

# Initialize variables
lap = 0
start = 0
end = interval

# Find and save graph with minimum Laplacian energy
while end-interval <= len(graphs_tuple)+1:
    for graph in graphs_tuple[start:end]:
        new_spectrum = graph[1].spectrum(laplacian=True)
        new_energy = le(new_spectrum, n, m)
        new_index = graph[0]
        if new_energy < energy:
            spectrum = new_spectrum
            energy = new_energy
            graph_tuple = graph[1]
            index = new_index

            # Save graph information
            save_graph(graphs[index], n, index) 
            write_energy(index, n, energy)
    start += interval
    end += interval
    lap += 1

# time_end = time.time()
sigma = sigma(graph_tuple, spectrum)
diameter = diameter(graph_tuple)
# time = time_end-time_start
# print(time)

# TO DO
with open("energies.txt", "a") as file:
    file.writelines(["\nSigma: {sigma}", "\nDiameter: {diameter}"])
    file.close()

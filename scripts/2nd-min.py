#!/usr/bin/env sage -python

# import time
from sage.all import *
from functions import unicyclic_graphs
from functions import laplacian_energy as le

def find_min(energy):
    minimum = min(energy)
    index = energy.index(minimum)
    return index, minimum

def save_plot(index):
    file = f"{index:02}-min.png"
    graphs[index].plot().save(file)

# start = time.time()

# Set parameters
n, m = 10, 10  # Vertices and edges

# Generate graphs
graphs = list(unicyclic_graphs(n, m))

# Compute Laplacian energy for all graphs
energy = [le(graph.spectrum(laplacian=True), n, m) for graph in graphs]

# Find the lowest number
1st_min = find_min(energy)
print(f"1st LE min: {round(1st_min[1], 5)}")

# Delete the lowest number from list
del energy[index]

# Find the new lowest number
2nd_min = find_min(energy)
print(f"2nd LE min: {round(2nd_min[1], 5)}")

# Save graph plots as PNG
save_plot(1st_min[0])
save_plot(2nd_min[0])

# end = time.time()
# time = end-start

with open("2nd-min.txt", "w") as file:
    file.writelines([f"1st LE min: {1st_min[1]}\n", f"2nd LE min: {2nd_min[1]}\n"])
    # file.write(f"Time: {time}")
    file.close()

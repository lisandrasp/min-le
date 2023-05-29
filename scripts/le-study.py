#!/usr/bin/env sage -python

from sage.all import *
from functions import laplacian_energy as le

# Set parameters
n, m = 10, 10  # Vertices and edges
c = 4          # Cycle vertices

# Tadpole graph
tadpole = graphs.TadpoleGraph(c, n-c)
tp_le = round(le(tadpole.spectrum(laplacian=True), n, m), 5)
tp_plot = tadpole.plot()+text(f"$LE(T)={tp_le}$",
                              (0,0),
                              horizontal_alignment='left')

# Cycle graph
cycle = graphs.CycleGraph(n)
cl_le = round(le(cycle.spectrum(laplacian=True), n, m), 5)
cl_plot = cycle.plot()+text(f"$LE(C)={cl_le}$",
                            (0,0),
                            horizontal_alignment='right')

# Save graph plots as PNG
plot = graphics_array([tp_plot, cl_plot])
plot.save("le-study.png")

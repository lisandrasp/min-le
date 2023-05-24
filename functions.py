def unicyclic_graphs(n, m):
    '''Generate and return a list of non-isomorphic unicyclic graphs.'''
    parameters = str(n)+" -c "+str(m)+":"+str(m)
    graphs = list(graphs.nauty_geng(parameters))
    return graphs

def laplacian_energy(spectrum, n, m):
    '''Compute and return the Laplacian energy of a graph.'''
    sum = 0
    for eigenvalue in spectrum:
        sum += abs((eigenvalue-2) * (m/n))
    return sum

def sigma(graph, spectrum):
    '''Find and return the Sigma of a graph.'''
    degree = graph.average_degree()
    sigma = len([eigenvalue for eigenvalue in spectrum if eigenvalue >= degree])
    return sigma

def diameter(graph):
    '''Find and return the diameter of a graph.'''
     geodesic = graph.distance_all_pairs()
     distances = set()
     for path in geodesic:
         for distance in geodesic[path].values():
            distances.add(distance)
    diameter = max(distances)
    return diameter

def save_graph(graph, n, index):
    '''Save graph plot as a PNG file.'''
    image_name = "g{:02}{:02}.png"
    graph.plot().save(image_name.format(n, index))

def write_energy(index, n, energy):
    '''Write row into the energies table'''
    file = open("energies.txt", "a")
    row = "| {:1} | {:1} | {:^6} |\n"
    file.write(row.format(index, n, energy))
    file.close()

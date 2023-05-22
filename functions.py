def laplacian_energy(spectrum, n, m):
    """
    Calculates the Laplacian energy of a graph.

    Parameters:
        spectrum (list): A list of Laplacian eigenvalues.
        n (int): The number of vertices.
        m (int): The number of edges.

    Returns:
        sum (float): The Laplacian energy of a graph.
    """

    sum = 0
    for mu in spectrum:
        sum += abs((mu-2)*(m/n))
    return sum

def sigma(graph, spectrum):
    """
    Calculates the Sigma of a graph.

    Sigma is the number of laplacian eigenvalues greater or equal to the average degree.

    Parameters:
        graph (graph): A graph.
        spectrum (list): A list of Laplacian eigenvalues.

    Returns:
        sigma_value (int): The value of Sigma.
    """

    degree = graph.average_degree()
    sigma_value = len([mu for mu in spectrum if mu >= degree])
    return sigma_value

def diameter(graph):
    """
    Calculates the diameter of a graph.

    Diameter is the length of the "longest shortest path" between any two vertices.

    Parameters:
        graph (graph): A graph.

    Returns:
        distance_maximum (int): The diameter of a graph.
    """

    distance_all = graph.distance_all_pairs()
    distance_set = set()
    for dictionary in distance_all:
        for distance in distance_all[dictionary].values():
            distance_set.add(distance)
    distance_maximum = max(distance_set)
    return distance_maximum

import networkx as nx


def prim(graph: nx.Graph):
    start_node = 0
    costs = {}
    neighbors = {}
    for node in graph.nodes:
        if node == start_node:
            continue
        elif graph.has_edge(start_node, node):
            costs[node] = graph.edges[start_node, node]["weight"]
            neighbors[node] = start_node
        else:
            costs[node] = float("inf")
            neighbors[node] = start_node

    unprocessed_nodes = set(graph.nodes) - {start_node}
    minimum_spanning_tree = nx.Graph()
    while len(unprocessed_nodes) != 0:
        nearest_node = -1
        min_ = float("inf")
        for node in unprocessed_nodes:
            if costs[node] < min_:
                min_ = costs[node]
                nearest_node = node

        unprocessed_nodes.remove(nearest_node)
        minimum_spanning_tree.add_edges_from([(nearest_node, neighbors[nearest_node])])

        for node in unprocessed_nodes:
            if (
                graph.has_edge(nearest_node, node)
                and graph.edges[nearest_node, node]["weight"] < costs[node]
            ):
                costs[node] = graph.edges[nearest_node, node]["weight"]
                neighbors[node] = nearest_node

    return minimum_spanning_tree

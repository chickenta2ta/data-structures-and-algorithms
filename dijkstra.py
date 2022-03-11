import networkx as nx
import heapq as hq


def dijkstra(graph: nx.DiGraph, start_node: str):
    costs = {}
    for node in graph.nodes:
        if node == start_node:
            continue
        elif graph.has_edge(start_node, node):
            costs[node] = graph.edges[start_node, node]["weight"]
        else:
            costs[node] = float("inf")
    heap = []
    for node, cost in costs.items():
        hq.heappush(heap, (cost, node))
    while len(heap) != 0:
        node = hq.heappop(heap)
        for neighbor in graph.neighbors(node[1]):
            if (
                costs[node[1]] + graph.edges[node[1], neighbor]["weight"]
                < costs[neighbor]
            ):
                costs[neighbor] = (
                    costs[node[1]] + graph.edges[node[1], neighbor]["weight"]
                )
                hq.heapify(heap)
    return costs

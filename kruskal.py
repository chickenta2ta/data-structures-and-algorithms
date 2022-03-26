import networkx as nx
import heapq as hq
from merge_find_set import MergeFindSet


def kruskal(graph: nx.Graph):
    minimum_spanning_tree = nx.Graph()

    heap = []
    for edge in graph.edges:
        hq.heappush(heap, (graph.get_edge_data(*edge)["weight"], edge))
    subtrees = MergeFindSet(graph.nodes)

    while len(heap) != 0:
        edge = hq.heappop(heap)
        subtree1 = subtrees.find(edge[1][0])
        subtree2 = subtrees.find(edge[1][1])
        if subtree1 != subtree2:
            minimum_spanning_tree.add_edge(*edge[1])
            subtrees.merge(subtree1, subtree2)

    return minimum_spanning_tree

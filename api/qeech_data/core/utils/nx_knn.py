import networkx as nx


def __shortest_path_length_catch(graph: nx.Graph, source, target):
    try:
        return nx.shortest_path_length(graph, source=source, target=target)
    except nx.NetworkXNoPath:
        return float("inf")


def nx_knn(graph: nx.Graph, searching_node, n: int, *, label: str | None = None):
    return list(
        map(
            lambda x: x[0],
            sorted(
                [
                    (node, __shortest_path_length_catch(graph, source=searching_node, target=node[0]))
                    for node in graph.nodes(data=True)
                    if label is None or node[1]["label"] == label
                ],
                key=lambda x: x[1],
            )[:n],
        )
    )

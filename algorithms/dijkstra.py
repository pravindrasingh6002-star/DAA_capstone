
"""
Dijkstra's Shortest Path Algorithm
Used for finding shortest delivery paths.
"""

import heapq


def dijkstra(graph, start):
    """
    Find shortest distances from start
    to all reachable vertices.

    Graph format:
    {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1},
        "C": {"A": 2, "B": 1}
    }
    """

    if start not in graph:
        raise ValueError("Starting location not found.")

    for neighbors in graph.values():
        for weight in neighbors.values():
            if weight < 0:
                raise ValueError(
                    "Dijkstra requires non-negative edge weights."
                )

    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            new_distance = current_distance + weight

            if new_distance < distances.get(neighbor, float("inf")):

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def reconstruct_path(previous, start, destination):
    """
    Reconstruct the shortest path
    using the previous-node dictionary.
    """

    if destination not in previous:
        return []

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path

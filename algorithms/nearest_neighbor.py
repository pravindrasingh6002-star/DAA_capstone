
"""
Nearest Neighbor TSP Approximation
Used for courier route optimization.
"""


def nearest_neighbor_tsp(distance_matrix, start):
    """
    Generate a delivery route using
    the Nearest Neighbor approach.

    distance_matrix format:
    {
        "A": {"A": 0, "B": 4, "C": 2},
        "B": {"A": 4, "B": 0, "C": 1},
        "C": {"A": 2, "B": 1, "C": 0}
    }

    Returns route and total distance.
    """

    if start not in distance_matrix:
        raise ValueError("Starting location not found.")

    locations = list(distance_matrix.keys())

    if any(set(locations) - set(distance_matrix[node])
           for node in locations):
        raise ValueError("Distance matrix must be complete.")

    unvisited = set(locations)
    unvisited.remove(start)

    route = [start]
    current = start
    total_distance = 0

    while unvisited:

        nearest = min(
            unvisited,
            key=lambda location: distance_matrix[current][location]
        )

        distance = distance_matrix[current][nearest]

        if distance == float("inf"):
            raise ValueError("Some locations are unreachable.")

        total_distance += distance

        route.append(nearest)
        unvisited.remove(nearest)

        current = nearest

    # Return to starting location
    if len(locations) > 1:

        return_distance = distance_matrix[current][start]

        if return_distance == float("inf"):
            raise ValueError("Cannot return to starting location.")

        total_distance += return_distance
        route.append(start)

    return {
        "route": route,
        "total_distance": total_distance
    }

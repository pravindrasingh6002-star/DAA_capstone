
"""
Route Manager Module
Mini-Courier Planner - DAA Capstone

Responsibilities:
1. Load delivery location data.
2. Calculate shortest paths using Dijkstra.
3. Build an all-pairs shortest-distance matrix.
4. Generate delivery routes using Nearest Neighbor TSP.
5. Display the final delivery route and distance.
"""

import json
from pathlib import Path

from algorithms import dijkstra, reconstruct_path
from algorithms import nearest_neighbor_tsp


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "locations.json"
)


def load_locations():
    """Load delivery locations and road network."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("Error: locations.json not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid locations JSON.")
        return None


def calculate_all_pairs_shortest_paths(graph, locations):
    """
    Run Dijkstra from every location to calculate
    the shortest distance between every pair.
    """

    distance_matrix = {}
    path_matrix = {}

    for source in locations:

        distances, previous = dijkstra(graph, source)

        distance_matrix[source] = {}
        path_matrix[source] = {}

        for destination in locations:

            distance_matrix[source][destination] = (
                distances[destination]
            )

            path_matrix[source][destination] = (
                reconstruct_path(
                    previous,
                    source,
                    destination
                )
            )

    return distance_matrix, path_matrix


def generate_delivery_route(distance_matrix, depot):
    """Generate an approximate route using Nearest Neighbor."""

    return nearest_neighbor_tsp(distance_matrix, depot)


def display_route_result(result, path_matrix):
    """Display final route and shortest road paths."""

    route = result["route"]

    print("\n" + "=" * 60)
    print("              COURIER DELIVERY ROUTE")
    print("=" * 60)

    print("\nOptimized Delivery Sequence:")

    print(" -> ".join(route))

    print("\nIndividual Road Paths:")

    for i in range(len(route) - 1):

        source = route[i]
        destination = route[i + 1]

        path = path_matrix[source][destination]

        print(
            f"{source} to {destination}: "
            + " -> ".join(path)
        )

    print("\nTotal Delivery Distance:",
          result["total_distance"], "km")

    print("=" * 60)


def run_route_manager():
    """Execute the complete route planning process."""

    data = load_locations()

    if data is None:
        return None

    graph = data["graph"]
    locations = data["locations"]
    depot = data["depot"]

    # Step 1: Calculate shortest distances
    distance_matrix, path_matrix = (
        calculate_all_pairs_shortest_paths(
            graph, locations
        )
    )

    print("\nDijkstra shortest paths calculated successfully!")

    # Step 2: Generate approximate delivery route
    result = generate_delivery_route(
        distance_matrix, depot
    )

    print("Nearest Neighbor route generated successfully!")

    # Step 3: Display final results
    display_route_result(result, path_matrix)

    return result


if __name__ == "__main__":
    run_route_manager()

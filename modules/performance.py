
"""
Performance Testing Module
Mini-Courier Planner - DAA Capstone

Measures execution time of:
1. Merge Sort
2. Knapsack
3. Dijkstra
4. Nearest Neighbor TSP
"""

import csv
import random
import time
import statistics
from pathlib import Path

from algorithms import (
    merge_sort,
    knapsack,
    dijkstra,
    nearest_neighbor_tsp
)

ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / "results"
CSV_FILE = RESULTS_DIR / "runtime_results.csv"


def measure_runtime(function, *args, repeats=3):
    """Return median execution time in seconds."""
    times = []

    for _ in range(repeats):
        start = time.perf_counter()
        function(*args)
        end = time.perf_counter()
        times.append(end - start)

    return statistics.median(times)


def generate_parcels(size):
    rng = random.Random(42)

    return [
        {
            "id": f"P{i}",
            "destination": "A",
            "weight": rng.randint(1, 20),
            "value": rng.randint(10, 200),
            "priority": rng.randint(1, 5),
            "deadline": rng.randint(1, 10)
        }
        for i in range(size)
    ]


def generate_graph(size):
    """Generate a connected, undirected weighted graph."""
    rng = random.Random(42)
    graph = {str(i): {} for i in range(size)}

    for i in range(size):
        for j in range(i + 1, size):
            weight = rng.randint(1, 100)
            graph[str(i)][str(j)] = weight
            graph[str(j)][str(i)] = weight

    return graph


def generate_distance_matrix(size):
    rng = random.Random(42)

    return {
        str(i): {
            str(j): (0 if i == j else rng.randint(1, 100))
            for j in range(size)
        }
        for i in range(size)
    }


def run_benchmarks():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    print("\nStarting Performance Testing...")
    print("-" * 55)

    # 1. Merge Sort and Knapsack
    for size in [50, 100, 200, 500]:
        parcels = generate_parcels(size)

        sort_time = measure_runtime(merge_sort, parcels)
        results.append(["Merge Sort", size, sort_time])

        knapsack_time = measure_runtime(knapsack, parcels, 1000)
        results.append(["Knapsack DP", size, knapsack_time])

    # 2. Dijkstra and Nearest Neighbor
    for size in [20, 40, 60, 80]:
        graph = generate_graph(size)
        matrix = generate_distance_matrix(size)

        dijkstra_time = measure_runtime(dijkstra, graph, "0")
        results.append(["Dijkstra", size, dijkstra_time])

        tsp_time = measure_runtime(
            nearest_neighbor_tsp, matrix, "0"
        )
        results.append(["Nearest Neighbor TSP", size, tsp_time])

    # Save results to CSV
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Algorithm",
            "Dataset Size",
            "Runtime Seconds"
        ])
        writer.writerows(results)

    print("\nPerformance Testing Completed!")
    print("-" * 55)

    print(f"{'Algorithm':<25} {'Size':<10} {'Time (seconds)':<18}")
    print("-" * 55)

    for algorithm, size, runtime in results:
        print(f"{algorithm:<25} {size:<10} {runtime:<18.8f}")

    print("-" * 55)
    print(f"\nCSV file saved at: {CSV_FILE}")


if __name__ == "__main__":
    run_benchmarks()

def generate_performance_charts():
    import matplotlib.pyplot as plt

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    charts_dir = RESULTS_DIR / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    algorithms = [
        "Merge Sort",
        "Knapsack DP",
        "Dijkstra",
        "Nearest Neighbor TSP"
    ]

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    for algorithm in algorithms:
        selected = [
            row for row in rows
            if row["Algorithm"] == algorithm
        ]

        sizes = [int(row["Dataset Size"]) for row in selected]
        runtimes = [
            float(row["Runtime Seconds"]) for row in selected
        ]

        plt.figure(figsize=(8, 5))
        plt.plot(sizes, runtimes, marker="o")
        plt.title(f"{algorithm} - Runtime Analysis")
        plt.xlabel("Dataset Size")
        plt.ylabel("Runtime (seconds)")
        plt.grid(True)

        filename = algorithm.lower().replace(" ", "_") + ".png"
        plt.savefig(charts_dir / filename, dpi=150)
        plt.close()

        print(f"Chart saved: {filename}")

    print("\nAll performance charts generated successfully!")


if __name__ == "__main__":
    generate_performance_charts()


"""
Parcel Manager Module
Mini-Courier Planner - DAA Capstone

Responsibilities:
1. Load parcel data from JSON.
2. Prioritize parcels using Merge Sort.
3. Select optimal parcels using 0/1 Knapsack.
4. Display parcel information and packing results.
"""

import json
from pathlib import Path

from algorithms import merge_sort, knapsack


# Project data file
DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "parcels.json"
)


def load_parcels():
    """Load parcel information from the JSON dataset."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            parcels = json.load(file)

        return parcels

    except FileNotFoundError:
        print("Error: parcels.json file not found.")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def prioritize_parcels(parcels):
    """Sort parcels using Merge Sort."""

    return merge_sort(parcels)


def optimize_packing(parcels, capacity):
    """Select optimal parcels using 0/1 Knapsack."""

    return knapsack(parcels, capacity)


def display_parcels(parcels):
    """Display parcel information."""

    print("\n" + "=" * 75)
    print("                  PARCEL PRIORITIZATION")
    print("=" * 75)

    print(
        f"{'ID':<10}"
        f"{'Destination':<15}"
        f"{'Weight':<10}"
        f"{'Value':<10}"
        f"{'Priority':<10}"
        f"{'Deadline':<10}"
    )

    print("-" * 75)

    for parcel in parcels:
        print(
            f"{parcel['id']:<10}"
            f"{parcel['destination']:<15}"
            f"{parcel['weight']:<10}"
            f"{parcel['value']:<10}"
            f"{parcel['priority']:<10}"
            f"{parcel['deadline']:<10}"
        )

    print("=" * 75)


def display_packing_result(result):
    """Display the optimal packing result."""

    print("\n" + "=" * 55)
    print("              OPTIMAL PACKING PLAN")
    print("=" * 55)

    print("\nSelected Parcels:")

    for parcel in result["selected_parcels"]:
        print(
            f"{parcel['id']} | "
            f"Weight: {parcel['weight']} | "
            f"Value: {parcel['value']}"
        )

    print("-" * 55)
    print("Total Weight:", result["total_weight"])
    print("Total Value:", result["total_value"])
    print("Remaining Capacity:", result["remaining_capacity"])
    print("=" * 55)


def run_parcel_manager(capacity=15):
    """Run the complete parcel management process."""

    parcels = load_parcels()

    if not parcels:
        print("No parcel data available.")
        return None

    # Step 1: Sort parcels
    sorted_parcels = prioritize_parcels(parcels)

    print("\nParcels sorted successfully using Merge Sort!")

    display_parcels(sorted_parcels)

    # Step 2: Optimize package selection
    result = optimize_packing(sorted_parcels, capacity)

    print("\nKnapsack optimization completed successfully!")

    display_packing_result(result)

    return result


if __name__ == "__main__":
    run_parcel_manager()

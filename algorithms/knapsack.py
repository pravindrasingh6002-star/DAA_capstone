
"""
0/1 Knapsack Algorithm
Used for optimal parcel selection.
"""


def knapsack(parcels, capacity):
    """
    Select parcels with maximum total value
    without exceeding vehicle capacity.

    Each parcel can be selected only once.

    Returns:
        Dictionary containing selected parcels,
        total weight, total value and DP table.
    """

    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")

    if any(p["weight"] < 0 or p["value"] < 0 for p in parcels):
        raise ValueError("Weight and value cannot be negative.")

    n = len(parcels)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            # Exclude current parcel
            dp[i][w] = dp[i - 1][w]

            # Include current parcel if possible
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    # Backtrack to find selected parcels
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected.reverse()

    total_weight = sum(p["weight"] for p in selected)
    total_value = sum(p["value"] for p in selected)

    return {
        "selected_parcels": selected,
        "total_weight": total_weight,
        "total_value": total_value,
        "remaining_capacity": capacity - total_weight,
        "dp_table": dp
    }

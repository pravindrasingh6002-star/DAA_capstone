
# 🚚 Mini-Courier Planner
### Design and Analysis of Algorithms (DAA) Capstone Project

A Python-based courier optimization application that prioritizes
parcels, optimizes package selection, calculates shortest delivery
paths, and analyzes algorithm performance.

---

## 📌 Project Overview

Mini-Courier Planner is designed to demonstrate the practical
application of Design and Analysis of Algorithms concepts in a
courier delivery system.

It integrates sorting, dynamic programming, graph algorithms,
and performance analysis into one application.

## 🎯 Project Objectives

- Prioritize parcels according to priority and deadlines.
- Select the most valuable parcels within a weight capacity.
- Calculate shortest paths between delivery locations.
- Generate an approximate delivery route.
- Compare algorithm execution times.

## ✨ Features

- Parcel prioritization using Merge Sort.
- Optimal package selection using 0/1 Knapsack DP.
- Shortest path calculation using Dijkstra's Algorithm.
- Delivery route generation using Nearest Neighbor TSP.
- Runtime performance measurement.
- Automatic performance chart generation.
- JSON-based input datasets.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| JSON | Input data storage |
| Matplotlib | Performance charts |
| CSV | Runtime results |
| VS Code | Development environment |
| Git & GitHub | Version control |

## 🧠 Algorithms and Complexity

| Algorithm | Purpose | Time Complexity |
|---|---|---|
| Merge Sort | Parcel sorting | O(n log n) |
| 0/1 Knapsack DP | Parcel selection | O(nW) |
| Dijkstra | Shortest paths | O((V+E) log V) |
| Nearest Neighbor TSP | Route approximation | O(V²) |

## 📂 Project Structure

```text
Mini-Courier-Planner/
│
├── algorithms/
│   ├── __init__.py
│   ├── merge_sort.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── nearest_neighbor.py
│
├── data/
│   ├── parcels.json
│   └── locations.json
│
├── modules/
│   ├── __init__.py
│   ├── parcel_manager.py
│   ├── route_manager.py
│   └── performance.py
│
├── results/
│   ├── charts/
│   └── runtime_results.csv
│
├── screenshots/
│
├── docs/
│   └── project_report.md
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Mini-Courier-Planner
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

## ▶️ Application Menu

```text
=======================================================
             MINI-COURIER PLANNER
=======================================================
1. Parcel Prioritization and Box Filling
2. Shortest Paths and Delivery Route
3. Run Complete Courier Planning
4. Exit
=======================================================
```

## 📊 Sample Results

### Parcel Optimization

- Total selected weight: 15
- Total selected value: 340
- Remaining capacity: 0

Selected parcels:

- P105
- P107
- P103
- P106

### Delivery Route

```text
DEPOT -> A -> B -> C -> D -> DEPOT
```

**Total delivery distance: 25 km**

## 📈 Performance Analysis

The project measures the execution time of:

1. Merge Sort
2. Knapsack Dynamic Programming
3. Dijkstra's Algorithm
4. Nearest Neighbor TSP

Results are stored in:

- `results/runtime_results.csv`
- `results/charts/`

## 📷 Screenshots

Project screenshots will be available in the `screenshots/`
folder.

## 🔮 Future Improvements

- Graphical user interface.
- Real-world map integration.
- Live parcel tracking.
- Multiple courier vehicle support.
- Database integration.
- Traffic-aware route optimization.

## 🎓 Conclusion

Mini-Courier Planner demonstrates the integration of
fundamental algorithmic techniques into a practical
courier delivery optimization system.

## 📚 References

- Introduction to Algorithms — Cormen, Leiserson, Rivest, and Stein.
- Python Documentation: https://docs.python.org/3/
- Matplotlib Documentation: https://matplotlib.org/

---

**Project:** Mini-Courier Planner  
**Course:** Design and Analysis of Algorithms  
**Course Code:** ETCCDA302  
**Language:** Python

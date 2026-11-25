
# MINI-COURIER PLANNER
## Design and Analysis of Algorithms Capstone Project

**Course:** Design and Analysis of Algorithms  
**Course Code:** ETCCDA302  
**Language:** Python  
**Project Type:** Courier Delivery Optimization System

---

## 1. Introduction

Mini-Courier Planner is a Python-based application designed to
optimize parcel selection, package prioritization, and courier
delivery routes.

The project integrates sorting, dynamic programming, graph
algorithms, and performance analysis.

## 2. Objectives

- Prioritize parcels based on priority and delivery deadlines.
- Select valuable parcels within a fixed carrying capacity.
- Calculate shortest delivery paths.
- Generate an approximate delivery route.
- Analyze algorithm execution time.

## 3. Algorithms Used

### 3.1 Merge Sort
Used to sort parcels by priority and deadline.

Time Complexity: O(n log n)  
Space Complexity: O(n)

### 3.2 0/1 Knapsack Dynamic Programming
Used to select parcels that maximize total value without
exceeding the carrying capacity.

Time Complexity: O(nW)  
Space Complexity: O(nW)

### 3.3 Dijkstra's Algorithm
Used to calculate shortest paths between delivery locations.

Time Complexity: O((V + E) log V)  
Space Complexity: O(V + E)

### 3.4 Nearest Neighbor TSP Approximation
Used to generate a delivery sequence by repeatedly selecting
the nearest unvisited location.

Time Complexity: O(V^2)  
Space Complexity: O(V)

## 4. System Architecture

The project contains four main layers:

1. Algorithms: Sorting, Knapsack, Dijkstra, and TSP.
2. Modules: Parcel management, route management, and performance.
3. Data: Parcel and location JSON files.
4. Main Application: Integrates all modules through a menu.

## 5. Implementation

The application provides three main operations:

- Parcel Prioritization and Box Filling
- Shortest Paths and Delivery Route
- Complete Courier Planning

The application uses JSON files for input data and Python
modules for algorithm implementation.

## 6. Sample Results

### Parcel Optimization

Total selected weight: 15  
Total selected value: 340  
Remaining capacity: 0

Selected parcels:

- P105
- P107
- P103
- P106

### Delivery Route

DEPOT -> A -> B -> C -> D -> DEPOT

Total delivery distance: 25 km

### Performance Testing

Runtime measurements are stored in:

results/runtime_results.csv

Performance charts are stored in:

results/charts/

## 7. Performance Analysis

The application measures execution time for:

- Merge Sort
- Knapsack Dynamic Programming
- Dijkstra's Algorithm
- Nearest Neighbor TSP

The measurements help compare execution time as dataset
sizes increase.

## 8. Limitations

- Nearest Neighbor TSP is an approximation and may not produce
  the globally shortest tour.
- The application uses sample delivery data.
- Knapsack performance depends on the capacity value.
- Real-world traffic and changing road conditions are not modeled.

## 9. Future Scope

- Add a graphical user interface.
- Integrate real-world maps and traffic information.
- Store delivery records in a database.
- Support multiple courier vehicles.
- Add live parcel tracking.

## 10. Conclusion

Mini-Courier Planner demonstrates how fundamental Design and
Analysis of Algorithms concepts can be integrated into a
practical courier optimization application.

The project combines sorting, dynamic programming, shortest
path algorithms, approximate TSP, and runtime analysis in
one Python application.

## 11. References

- Introduction to Algorithms - Cormen, Leiserson, Rivest, and Stein.
- Python Official Documentation: https://docs.python.org/3/
- Python time Module: https://docs.python.org/3/library/time.html
- Matplotlib Documentation: https://matplotlib.org/stable/

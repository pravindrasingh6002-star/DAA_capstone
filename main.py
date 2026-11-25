
"""
Mini-Courier Planner
DAA Capstone Project
Main Application
"""

from modules.parcel_manager import run_parcel_manager
from modules.route_manager import run_route_manager


def display_menu():
    print("\n" + "=" * 55)
    print("             MINI-COURIER PLANNER")
    print("=" * 55)
    print("1. Parcel Prioritization and Box Filling")
    print("2. Shortest Paths and Delivery Route")
    print("3. Run Complete Courier Planning")
    print("4. Exit")
    print("=" * 55)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            run_parcel_manager()

        elif choice == "2":
            run_route_manager()

        elif choice == "3":
            print("\nRUNNING COMPLETE COURIER PLANNING")
            run_parcel_manager()
            run_route_manager()

        elif choice == "4":
            print("\nThank you for using Mini-Courier Planner!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

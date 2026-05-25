import csv
import os

FILE = "sports.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Sport", "Category", "Popularity"])

def add_data():
    sport = input("Enter sport name: ")
    category = input("Enter category (Team/Individual): ")
    popularity = input("Enter popularity (1-100): ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sport, category, popularity])

    print("✅ Data added successfully")

def view_data():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def search_data():
    keyword = input("Enter sport to search: ").lower()

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if keyword in row[0].lower():
                print(row)

def menu():
    init_file()

    while True:
        print("\n--- Sports Research System ---")
        print("1. Add Data")
        print("2. View Data")
        print("3. Search Data")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            search_data()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()

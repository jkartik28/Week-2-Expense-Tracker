import csv
import os
from datetime import datetime

# ==============================
# Personal Expense Tracker (CLI)
# ==============================

FILE_NAME = "expenses.csv"


# Create CSV file if it does not exist
def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Category",
                "Description",
                "Amount"
            ])


# Display project title
def title():

    print("\n" + "=" * 50)
    print("        PERSONAL EXPENSE TRACKER")
    print("=" * 50)


# Add a new expense
def add_expense():

    title()

    print("Add New Expense\n")

    date = datetime.now().strftime("%d-%m-%Y")

    category = input("Enter Category : ").strip().title()

    description = input("Enter Description : ").strip()

    if category == "" or description == "":

        print("\nCategory and Description cannot be empty.")

        return

    try:

        amount = float(input("Enter Amount (₹): "))

    except ValueError:

        print("\nPlease enter a valid amount.")

        return

    if amount <= 0:

        print("\nAmount should be greater than zero.")

        return

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            date,
            category,
            description,
            amount
        ])

    print("\nExpense Added Successfully.")


# View all expenses
def view_expenses():

    title()

    print("Expense History\n")

    if not os.path.exists(FILE_NAME):

        print("Expense file not found.")

        return

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        records = list(reader)

    if len(records) <= 1:

        print("No expenses available.")

        return

    print("-" * 75)

    print("{:<12} {:<15} {:<25} {:>10}".format(
        "Date",
        "Category",
        "Description",
        "Amount"
    ))

    print("-" * 75)

    total = 0

    for row in records[1:]:

        date = row[0]
        category = row[1]
        description = row[2]
        amount = float(row[3])

        total += amount

        print("{:<12} {:<15} {:<25} ₹{:>8.2f}".format(
            date,
            category,
            description,
            amount
        ))

    print("-" * 75)
    print(f"Total Records : {len(records)-1}")
    print(f"Total Expense : ₹{total:.2f}")


# Search Expense
def search_expense():

    title()

    keyword = input("Enter Category or Description : ").strip().lower()

    if keyword == "":

        print("Search value cannot be empty.")
        return

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        records = list(reader)

    found = False

    print("\n" + "-" * 75)

    print("{:<12} {:<15} {:<25} {:>10}".format(
        "Date",
        "Category",
        "Description",
        "Amount"
    ))

    print("-" * 75)

    for row in records[1:]:

        if keyword in row[1].lower() or keyword in row[2].lower():

            print("{:<12} {:<15} {:<25} ₹{:>8.2f}".format(
                row[0],
                row[1],
                row[2],
                float(row[3])
                ))

            found = True

    if not found:


        print("No matching expense found.")

    print("-" * 75)


# Total Expense
def total_expense():

    if not os.path.exists(FILE_NAME):
        print("Expense file not found.")
        return

    total = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)
        next(reader, None)

        for row in reader:

            total += float(row[3])

    print("\nYour Total Expense is : ₹{:.2f}".format(total))


# Category Summary
def category_summary():

    if not os.path.exists(FILE_NAME):
        print("Expense file not found.")
        return

    title()

    summary = {}

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            category = row[1]
            amount = float(row[3])

            if category in summary:

                summary[category] += amount

            else:

                summary[category] = amount

    print("\nCategory Wise Expense\n")

    print("-" * 40)

    print("{:<20} {:>10}".format(
        "Category",
        "Amount"
    ))

    print("-" * 40)

    for category, amount in summary.items():

        print("{:<20} ₹{:>8.2f}".format(
            category,
            amount
        ))

    print("-" * 40)

    # Edit Expense
def edit_expense():

    if not os.path.exists(FILE_NAME):
        print("Expense file not found.")
        return

    title()

    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("No expense records found.")
        return

    print("\nAvailable Expenses:\n")

    for index, row in enumerate(reader[1:], start=1):
        print(f"{index}. {row[0]} | {row[1]} | {row[2]} | ₹{row[3]}")

    try:
        choice = int(input("\nEnter record number to edit : "))
    except ValueError:
        print("Invalid input.")
        return

    if choice < 1 or choice >= len(reader):
        print("Invalid record number.")
        return

    row = reader[choice]

    print("\nLeave blank to keep previous value.\n")

    category = input(f"Category ({row[1]}) : ").strip()
    description = input(f"Description ({row[2]}) : ").strip()
    amount = input(f"Amount ({row[3]}) : ").strip()

    if category != "":
        row[1] = category.title()

    if description != "":
        row[2] = description

    if amount != "":
        try:
            row[3] = str(float(amount))
        except ValueError:
            print("Invalid amount.")
            return

    reader[choice] = row

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(reader)

    print("\nExpense Updated Successfully.")


# Delete Expense
def delete_expense():

    if not os.path.exists(FILE_NAME):
        print("Expense file not found.")
        return

    title()

    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("No expense records found.")
        return

    print("\nExpense List\n")

    for index, row in enumerate(reader[1:], start=1):
        print(f"{index}. {row[0]} | {row[1]} | {row[2]} | ₹{row[3]}")

    try:
        choice = int(input("\nEnter record number to delete : "))
    except ValueError:
        print("Invalid input.")
        return

    if choice < 1 or choice >= len(reader):
        print("Invalid record number.")
        return

    del reader[choice]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(reader)

    print("\nExpense Deleted Successfully.")


# Monthly Summary
def monthly_summary():

    if not os.path.exists(FILE_NAME):
        print("Expense file not found.")
        return

    title()

    summary = {}

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            month = row[0][3:10]
            amount = float(row[3])

            if month in summary:
                summary[month] += amount
            else:
                summary[month] = amount

    print("\nMonthly Expense Summary\n")

    print("-" * 35)
    print("{:<15} {:>12}".format("Month", "Amount"))
    print("-" * 35)

    for month, amount in summary.items():

        print("{:<15} ₹{:>10.2f}".format(
            month,
            amount
        ))

    print("-" * 35)

    # Main Menu
def menu():

    create_file()

    while True:

        title()

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Total Expense")
        print("5. Category Summary")
        print("6. Edit Expense")
        print("7. Delete Expense")
        print("8. Monthly Summary")
        print("9. Exit")

        choice = input("\nEnter your choice : ").strip()

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            search_expense()

        elif choice == "4":

            total_expense()

        elif choice == "5":

            category_summary()

        elif choice == "6":

            edit_expense()

        elif choice == "7":

            delete_expense()

        elif choice == "8":

            monthly_summary()

        elif choice == "9":

            print("\n====================================")
            print(" Thank You For Using Expense Tracker ")
            print("====================================")
            break

        else:

            print("\nInvalid Choice. Please Try Again.")

        input("\nPress Enter to Continue...")


# Program Entry Point
if __name__ == "__main__":

    menu()
import sqlite3
import datetime

conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
''')
conn.commit()

def add_expense(amount, category, description):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)',
                   (amount, category, description, date))
    conn.commit()

def view_expenses():
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    return expenses

def view_spending_by_category(category):
    cursor.execute('SELECT * FROM expenses WHERE category = ?', (category,))
    category_expenses = cursor.fetchall()
    return category_expenses

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Spending by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            description = input("Enter a description (optional): ")
            add_expense(amount, category, description)
            print("Expense added successfully!")

        elif choice == "2":
            expenses = view_expenses()
            print("\nAll Expenses:")
            for expense in expenses:
                print(f"{expense[0]}. Amount: {expense[1]}, Category: {expense[2]}, Description: {expense[3]}, Date: {expense[4]}")

        elif choice == "3":
            category = input("Enter the category to view spending: ")
            category_expenses = view_spending_by_category(category)
            print(f"\nSpending for Category '{category}':")
            for expense in category_expenses:
                print(f"Amount: {expense[1]}, Description: {expense[3]}, Date: {expense[4]}")

        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
    conn.close()

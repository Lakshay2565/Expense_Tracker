from database import Database
from expense import Expense


class ExpenseTracker:

    def __init__(self):
        self.db = Database()

    # -----------------------------
    # Add Expense
    # -----------------------------
    def add_expense(self):

        print("\nAdd Expense\n")

        date = input("Date (DD-MM-YYYY): ")
        category = input("Category: ")
        description = input("Description: ")
        amount = float(input("Amount: "))

        expense = Expense(
            date,
            category,
            description,
            amount
        )

        self.db.cursor.execute(
            """
            INSERT INTO expenses
            (date, category, description, amount)
            VALUES (?, ?, ?, ?)
            """,
            (
                expense.date,
                expense.category,
                expense.description,
                expense.amount
            )
        )

        self.db.connection.commit()

        print("\nExpense Added Successfully!\n")

    # -----------------------------
    # View Expenses
    # -----------------------------
    def view_expenses(self):

        self.db.cursor.execute(
            "SELECT * FROM expenses ORDER BY date"
        )

        expenses = self.db.cursor.fetchall()

        if len(expenses) == 0:
            print("\nNo Expenses Found\n")
            return

        print()

        print("-" * 80)

        print(
            f"{'ID':<5}"
            f"{'DATE':<15}"
            f"{'CATEGORY':<15}"
            f"{'DESCRIPTION':<25}"
            f"{'AMOUNT'}"
        )

        print("-" * 80)

        for expense in expenses:

            print(
                f"{expense[0]:<5}"
                f"{expense[1]:<15}"
                f"{expense[2]:<15}"
                f"{expense[3]:<25}"
                f"{expense[4]}"
            )

    # -----------------------------
    # Delete Expense
    # -----------------------------
    def delete_expense(self):

        expense_id = input("\nExpense ID: ")

        self.db.cursor.execute(
            "SELECT * FROM expenses WHERE id=?",
            (expense_id,)
        )

        expense = self.db.cursor.fetchone()

        if expense is None:

            print("Expense not found.\n")
            return

        self.db.cursor.execute(
            "DELETE FROM expenses WHERE id=?",
            (expense_id,)
        )

        self.db.connection.commit()

        print("Expense Deleted Successfully.\n")

    # -----------------------------
    # Update Expense
    # -----------------------------
    def update_expense(self):

        expense_id = input("\nExpense ID: ")

        self.db.cursor.execute(
            "SELECT * FROM expenses WHERE id=?",
            (expense_id,)
        )

        expense = self.db.cursor.fetchone()

        if expense is None:

            print("Expense not found.\n")
            return

        print("\nLeave blank to keep old value.\n")

        date = input(f"Date ({expense[1]}): ")
        category = input(f"Category ({expense[2]}): ")
        description = input(f"Description ({expense[3]}): ")
        amount = input(f"Amount ({expense[4]}): ")

        if date == "":
            date = expense[1]

        if category == "":
            category = expense[2]

        if description == "":
            description = expense[3]

        if amount == "":
            amount = expense[4]

        self.db.cursor.execute(
            """
            UPDATE expenses
            SET
                date=?,
                category=?,
                description=?,
                amount=?
            WHERE id=?
            """,
            (
                date,
                category,
                description,
                float(amount),
                expense_id
            )
        )

        self.db.connection.commit()

        print("\nExpense Updated Successfully.\n")

    # -----------------------------
    # Search Category
    # -----------------------------
    def search_category(self):

        category = input("\nCategory: ")

        self.db.cursor.execute(
            """
            SELECT *
            FROM expenses
            WHERE LOWER(category)=LOWER(?)
            """,
            (category,)
        )

        expenses = self.db.cursor.fetchall()

        if len(expenses) == 0:

            print("\nNo Expenses Found\n")
            return

        print()

        for expense in expenses:

            print(expense)

    # -----------------------------
    # Monthly Summary
    # -----------------------------
    def monthly_summary(self):

        month = input("Month (MM): ")
        year = input("Year (YYYY): ")

        pattern = f"%-{month}-{year}"

        self.db.cursor.execute(
            """
            SELECT SUM(amount)
            FROM expenses
            WHERE date LIKE ?
            """,
            (pattern,)
        )

        total = self.db.cursor.fetchone()[0]

        if total is None:
            total = 0

        print(
            f"\nTotal Expense : ₹{total:.2f}\n"
        )

    # -----------------------------
    # Category Wise Summary
    # -----------------------------
    def category_summary(self):

        self.db.cursor.execute(
            """
            SELECT
                category,
                SUM(amount)
            FROM expenses
            GROUP BY category
            ORDER BY SUM(amount) DESC
            """
        )

        result = self.db.cursor.fetchall()

        print()

        print("-" * 35)

        print(
            f"{'CATEGORY':<20}"
            f"{'TOTAL'}"
        )

        print("-" * 35)

        for row in result:

            print(
                f"{row[0]:<20}"
                f"₹{row[1]:.2f}"
            )

        print()

    # -----------------------------
    # Close Database
    # -----------------------------
    def close(self):

        self.db.close()
from expense_tracker import ExpenseTracker


def main():

    tracker = ExpenseTracker()

    while True:

        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search by Category")
        print("6. Monthly Summary")
        print("7. Category Summary")
        print("8. Exit")
        print("=====================================")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            tracker.add_expense()

        elif choice == "2":

            tracker.view_expenses()

        elif choice == "3":

            tracker.update_expense()

        elif choice == "4":

            tracker.delete_expense()

        elif choice == "5":

            tracker.search_category()

        elif choice == "6":

            tracker.monthly_summary()

        elif choice == "7":

            tracker.category_summary()

        elif choice == "8":

            tracker.close()

            print("\nThank you for using Expense Tracker!")

            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
import os
from datetime import datetime
# os: ye check karne ke liye ki file exist karti hai ya nahi
# datetime: current date lene ke liye.



# File to store expenses
FILE_NAME = "expenses.txt" # FILE_NAME: ye file me hum sab expenses save karenge


# Utility Functions 

def load_expenses(): #Ye function file se data padhta hai (agar file pehle se bani ho)
    """Load expenses from file if exists."""
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",") #Har line ko split karta hai comma (,) se
                if len(parts) == 4:
                    name, category, amount, date = parts
                    expenses.append({ #Har line me ye 4 values hoti hain → name, category, amount, date
                        "name": name,
                        "category": category,
                        "amount": float(amount),
                        "date": date
                    })
    return expenses #Fir wo sab dictionary me convert karke expenses list me add karta hai
                       # Agar file nahi hai to empty list return karta hai


def save_expenses(expenses):
    """Save all expenses to file"""
    with open(FILE_NAME, "w") as file:
        for exp in expenses:
            file.write(f"{exp['name']},{exp['category']},{exp['amount']},{exp['date']}\n")
# Ye poori expenses list ko file me likhta hai
# Har dictionary ek line ban jaati hai file me (comma-separated format me)



#  Main Features 
def add_expense(expenses):
    """Add a new expense."""
    print("\n--- Add New Expense ---") #User se expense ka name, category, aur amount leta hai
    name = input("Enter expense name: ")
    category = input("Enter category (e.g. Food, Travel, Rent): ")
    try:
        amount = float(input("Enter amount: ")) #Agar amount number nahi hai to error deta hai
    except ValueError:
        print(" Invalid amount! Please enter numbers only.")
        return

    date = datetime.now().strftime("%Y-%m-%d") #Current date (YYYY-MM-DD format) le leta hai

    expenses.append({"name": name, "category": category, "amount": amount, "date": date}) #Fir naya expense dictionary banake expenses list me daalta ha
    save_expenses(expenses) #Fir us list ko file me save karta hai
    print(" Expense added successfully!") # sb set hone pr message print karta hai


def view_expenses(expenses): # new fuction to view expenses
    """View all expenses."""
    print("\n--- All Expenses ---") 
                                       
    if not expenses:
        print("No expenses recorded yet.")
        return # #Agar koi expense nahi hai → “No expenses” print karta ha

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} | {exp['category']} | ₹{exp['amount']} | {exp['date']}") 
        #ya phr sab expenses ko serial number ke saath line by line print karta hai


def category_summary(expenses):
    """Show total spent by category."""
    print("\n--- Expense Summary by Category ---")
    if not expenses:
        print("No data to summarize.") #Har category ka total amount calculate karta hain
        return

    summary = {} #summary ek dictionary hai jisme key = category, value = total amount
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"] 

    for cat, total in summary.items(): #Fir har category ka naam aur total print karta hai
        print(f"{cat}: ₹{total:.2f}")


def delete_expense(expenses):
    """Delete an expense by number.""" #Pehle sab expenses dikhaata hai
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index = int(input("\nEnter expense number to delete: ")) - 1 #User se expense number (index) maangta hai
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index) #Agar number valid hai to wo us entry ko delete kar deta hai list se
            save_expenses(expenses) #phir updated list ko file me save karta hai
            print(f"🗑 Deleted: {deleted['name']} ({deleted['category']})") 
        else:
            print(" Invalid number")
    except ValueError: #Delete hone ka message print karta hai
        print(" Please enter a valid number")


# Main Menu 
def main():
    expenses = load_expenses()

    while True:
        print("\n========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary by Category")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            category_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print(" Saving & Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Try again")
            
#Program start hote hi load_expenses() call hota hai (purane data ko laane ke liye).
# Menu show karta hai:
#  Add Expense, View Expenses, Summary, Delete Expense, Exit
# User ke input ke hisaab se function call hota hai.
# Jab user 5 dabata hai → program close ho jaata hai





# Run program
if __name__ == "__main__": #Ye line ensure karti hai ki jab ye file direct run karte ho (python expense_tracker.py) 
    main()                  #tabhi main() chale
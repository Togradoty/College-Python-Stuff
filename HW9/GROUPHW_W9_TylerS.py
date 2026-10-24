import matplotlib.pyplot as plt

def main():
    #sets up the different categories
    categories = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]
    expenses = []
    #looks through file and assigns numbers to categories
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                expenses.append(float(line.strip()))
    #deals with and explains certain issues
    except IOError:
        print("Could not open Expenses.txt")
        return
    except ValueError:
        print("Expenses.txt must only have six amounts")
        return
    #makes the graph
    plt.pie(expenses, labels=categories)
    plt.title("Monthly Expenses")
    plt.show()
#calls function
if __name__ == "__main__":
    main()
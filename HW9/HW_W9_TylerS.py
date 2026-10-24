import matplotlib.pyplot as plt

def main():
    #creates the lists to store prices and weeks
    gas_prices = []
    week_list = []

    try:
        #opens up the file to read gas prices
        with open("1994_Weekly_Gas_Averages.txt", "r") as file:
            for line in file:
                try:
                    gas_prices.append(float(line.strip()))
                except ValueError:
                    print("Value is not in the correct format, and Skipping the Value.")
        #create labels
        for week in range(1, len(gas_prices) + 1):
            week_list.append("Wk" + str(week))

        #print out lists
        print("Average gas prices=", gas_prices)
        print(week_list)

        #error test
        #print(gas_prices[90])

        #makes the graph
        plt.bar(week_list, gas_prices)
        plt.title("Average gas price in 1994")
        plt.xlabel("Week")
        plt.ylabel("Average price ($ per gallon)")
        plt.xticks(rotation=90)
        plt.ylim(0.95, 1.20)
        plt.grid(axis="y")
        plt.show()

    #errors and stuff
    except IOError:
        print("Text file not found.")
    except IndexError:
        print("There was an indexing error.")

if __name__ == "__main__":
    main()
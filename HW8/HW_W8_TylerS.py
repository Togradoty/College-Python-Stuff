#makes the initial sales list
sales = []
#trys to open the sales file, if it fails print out that there was an error
try:
    sales_file = open("sales_data.txt", "r")
#goes through the file and adds the data to sales list
    for line in sales_file:
        try:
            sales.append(float(line))
        except ValueError:
            #if it fails, say that it could not convert said line, and skip.
            print(f"Could not convert '{line.strip()}' to a number, skipping.")
    #closes out the file.
    sales_file.close()

    #sets up all of the differetn values for sales data.
    minimum_sales = min(sales)
    maximum_sales = max(sales)
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    #prints out the info
    print("Sales values:", sales)
    print(f"Minimum sales value: ${minimum_sales:,.2f}")
    print(f"Maximum sales value: ${maximum_sales:,.2f}")
    print(f"Total sales: ${total_sales:,.2f}")
    print(f"Average sales value: ${average_sales:,.2f}")


#says if there was an error
except IOError:
    print("Error, could not find or open sales_data.txt") 

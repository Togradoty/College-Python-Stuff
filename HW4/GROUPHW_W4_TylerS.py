#starts the total at zero and adds the total variable.
total = 0
#asks user for first number
number = float(input("Enter a positive number to start (or negative to quit): "))
#keeps asking for more/or to quit.
while number >=0:
    total = total + number
    number = float(input("Continue adding numbers, or do a negative number to quit: "))

#displays total
print(f"Total = {total:.2f}")

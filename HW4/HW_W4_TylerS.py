#asks for number
number = int(input("Input a non-negative number and this program will display it's factorial: "))
#makes sure number is above -1
while number < 0:
    print("Please enter a number larger than or equal to 0")
    number = int(input("Input a non-negative number and this program will display it's factorial: "))
#sets up factorial
factorial = 1
#calculation for factorial
for i in range(1, number + 1):
    factorial = factorial * i
#prints output
print(f"The Factorial of {number} is {factorial}")


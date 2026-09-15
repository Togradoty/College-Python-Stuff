#Asks the user for what temperature in celsius they would like to know in fahrenheit.
celsius = float(input("What is the Temperature in Celsius, that you want to know in Fahrenheit: "))
#sets up the conversion to fahrenheit from celsius.
fahrenheit = (9/5) * celsius + 32
#tells the user the converted temperature from celsius to fahrenheit.
print(f"{celsius:.2f} Celsius in Fahrenheit is: {fahrenheit:.2f}") 
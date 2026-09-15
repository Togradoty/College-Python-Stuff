#gets the age of the person
age = float(input("This program will tell you what age range the person falls into. How old is the person? "))
#goes through every possibility for what age the person could be. for whatever age group the person falls into the relating answer gets printed.
if age < 0:
    print("Incorrect Number")
elif age <= 1:
    print("This person is an Infant")
elif age <= 12:
    print("This person is a Child")
elif age <= 19:
    print("This person is a Teenager")
else: 
    print("This person is an Adult")

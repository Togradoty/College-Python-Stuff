#sets up the code to go through all numbers 1-10
def main():
    for time in range(1, 11):
        falling_distance(time)
#calculates the falling distance using gravity and the equation.
def falling_distance(time):
    gravity = 9.8
    distance = 0.5 * gravity * time ** 2
    print(f"{time} seconds {distance:.2f} meters")
#prints out the result
def topbit():
    print("Time      Falling Distance")
    print("--------------------------")
topbit()
main()
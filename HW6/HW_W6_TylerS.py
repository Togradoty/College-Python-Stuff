def main():
    for time in range(1, 11):
        falling_distance(time)

def falling_distance(time):
    gravity = 9.8
    distance = 0.5 * gravity * time ** 2
    print(f"{time} seconds {distance:.2f} meters")

def topbit():
    print("Time      Falling Distance")
    print("--------------------------")
topbit()
main()
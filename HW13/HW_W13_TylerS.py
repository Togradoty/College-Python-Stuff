from cars import Car

def main():
    #create my car
    my_car = Car(2016, "Volvo", "XC60")

    print("I am accelerating my car",
          my_car.get_year(), my_car.get_make(), my_car.get_model())
    #accelerates the car
    for i in range(5):
        my_car.accelerate()
        print(f"Speed of my car is= {my_car.get_speed()} mph")

    print("I am applying brakes to my car",
          my_car.get_year(), my_car.get_make(), my_car.get_model())
    #decelerates the car
    for i in range(5):
        my_car.brake()
        print(f"Speed of my car is = {my_car.get_speed()} mph")

if __name__ == "__main__":
    main()
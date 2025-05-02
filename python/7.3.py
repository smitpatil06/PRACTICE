class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")


def accelerate(car):
    print(f"{car.brand} is accelerating...")
    car.speed += 10
    print(f"New speed of {car.brand} is {car.speed} km/h")


c1 = Car("BMW", 80)
c1.show_info()

accelerate(c1)
c1.show_info()

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def display(self):
        print(f"Length: {self.length}, Breadth: {self.breadth}")

    def scale(self, factor):
        scaled_length = self.length * factor
        scaled_breadth = self.breadth * factor
        return Rectangle(scaled_length, scaled_breadth)


r1 = Rectangle(5, 3)
print("Original Rectangle:")
r1.display()

r2 = r1.scale(2)
print("Scaled Rectangle:")
r2.display()

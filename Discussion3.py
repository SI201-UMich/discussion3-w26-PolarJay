import math

class Rectangle():
    # Create the constructor "__init__" method

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Create the "__str__" method

    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"

    # Create the "area_calculator" method

    def area_calculator(self):
        return float(self.width) * float(self.height) 

    # Create the "__eq__" method

    # Returns a boolean value

    def __eq__(self, other):
        if self.width == other.width and self.height == other.height:
            return True
        else:
            return False


    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(f"r1: {r1}")
    # call the area_calculator method
    print("Area:", r1.area_calculator())
    print()

    r2 = Rectangle(10, 15)
    print(f"r2: {r2}")
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(f"Equal: r1 == r2? {r1 == r2}")
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    r3 = Rectangle(10, 15)
    print(f"r3: {r3}")
    print("Area:", r3.area_calculator())
    print(f"Equal: r2 == r3? {r2 == r3}")

if __name__ == "__main__":
    main()
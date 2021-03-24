class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (2 * (self.height + self.width))


R1 = Rectangle(4, 5)
R2 = Rectangle(9, 2)
print("area of rectangle1:", R1.area())
print("perimeter of rectangle1:", R1.perimeter())
print("area of rectangle2:", R2.area())
print("perimeter of rectangle2:", R2.perimeter())
if (R1.area() > R2.area()):
    print("Area of rectangle1 is greater than area of rectangle2")
else:
    print("Area of rectangle2 is greater than area of rectangle1")

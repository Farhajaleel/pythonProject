# write lambda function to find area of square , rectangle and triangle

square = lambda a: a * 2
print("Area of the square is", square(10))

rectangle = lambda a, b: a * b
print("Area of the rectangle is", rectangle(10, 5))

triangle = lambda b, h: (b * h) / 2
print("Area of the rectangle is", triangle(4, 2))

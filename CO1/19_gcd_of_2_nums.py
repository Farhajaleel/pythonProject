# Find gcd of two numbers

import math

a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
print("gcd of ", a, " and ", b, " is:", math.gcd(a, b))

# def GCD(a, b):
#     if a > b:
#         smaller = a
#     else:
#         smaller = b
#     for i in range(2, smaller + 1):
#         if a % i == 0 and b % i == 0:
#             g = i
#     return g
#
#
# a = int(input("Enter number1:"))
# b = int(input("Enter number2:"))
# print("Greatest common divisor of ", a, " and ", b, " is : ", GCD(a, b))

# find biggest of three numbers entered

biggest = int(input("Enter first number:"))
second = int(input("Enter the second number:"))
third = int(input("Enter third number:"))
if biggest < second:
    biggest = second
if biggest < third:
    biggest = third
print("biggest number is:", biggest)

# a = int(input("Enter 3 numbers:"))
# b = int(input())
# c = int(input())
# if (a > b) and (a > c):
#     print(a, "is largest number")
# elif (b > a) and (b > c):
#     print(b, "is largest number")
# else:
#     print(c, "is largest number")

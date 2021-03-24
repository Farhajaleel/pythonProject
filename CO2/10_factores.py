# Generate all factores of a number

num = int(input("Enter a number:"))
print("factors of number", num, "is\n")
for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        print(i)

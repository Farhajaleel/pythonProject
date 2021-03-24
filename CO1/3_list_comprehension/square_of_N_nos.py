#Square of n numbers

n=int(input("Enter the number of elements:"))
square=[i**2 for i in range(1,n+1)]
print(square)
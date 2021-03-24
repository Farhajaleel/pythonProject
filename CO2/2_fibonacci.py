# Generate fibonacci series of n numbers

def fibonacci(a, b, n):
    for i in range(n):
        print(a)
        a, b = b, a + b


limit = int(input("Enter the number of terms: "))
print("Fibonacci numbers upto ", limit, " terms are: ")
fibonacci(0, 1, limit)

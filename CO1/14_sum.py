# Accept an integer n and compute n+nn+nnn

num = input("Enter a number:")
result = 0
for i in range(1, 4):
    result = result + int(num * i)
print("result of", num, "+", num * 2, "+", num * 3, " = ", result)

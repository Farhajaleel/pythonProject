# Store a list of first names . Count the occurance of 'a' within the list

limit = int(input("Enter a limit:"))
firstName = [input("Enter the name:") for i in range(limit)]
for i in firstName:
    print("no of occurance of a in", i, "is", i.lower().count('a'))

# Display pyramiid with step number  accepted from user

num = int(input("Enter number of steps you want:"))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(i * j, end='\t')
    print(end='\n')

# construct the pattern using nested loop

for i in range(1, 10):
    j = 1
    if i > 5:
        limit = i - ((i % 5) * 2)
    else:
        limit = i
    while (j <= limit):
        print(end=" * ")
        j += 1
    print(end="\n")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(end=" * ")
#     print("\n")
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(end=" * ")
#     print("\n")

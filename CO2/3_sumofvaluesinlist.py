# find the sum of all the items in a list

list = []
limit = int(input("Enter the limit:"))
for i in range(limit):
    list.append(int(input("Enter number " + str(i + 1) + ":")))

print("List elements are:", list)
print("sum of elements in the list is:", sum(list))

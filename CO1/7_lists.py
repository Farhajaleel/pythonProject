
list1=list()
list2=list()
sum1=0
sum2=0


#Inputing values into the list
limit = int(input("Enter the limit:"))
for x in range(limit):
    num = int(input("Enter number " + str(x + 1) + ":"));
    list1.append(num)

limit = int(input("Enter the limit:"))
for x in range(limit):
    num = int(input("Enter number " + str(x + 1) + ":"));
    list2.append(num)

print(list1)
print(list2)

#checking whether lists are of same lenght
if(len(list1)==len(list2)):
    print("Two lists are of same length\n")
else:
    print("Two lists are of different length\n")

#printing sum of lists
sum1 = sum(list1)
print(sum1)
sum2 = sum(list2)
print(sum2)

#check wether sum of two lists are same
if(sum1==sum2):
    print("sum of elements in 2 lists are same\n")
else:
    print("sum of elements in 2 lists are not same\n")

#chech whether same value occur in the lists
for x in list1:
    if x in list2:
        print("Two lists have same value")
        break
else:
    print("Two lists haven't same value")



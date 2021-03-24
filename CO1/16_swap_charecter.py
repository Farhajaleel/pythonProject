# create a single string seperated with space from two strings by swapping the charecter at position 1

str1, str2 = input("Enter string 1:"), input("Enter string 2:")
print("String after swapping : "+str1[0]+str2[1]+str1[2:]+" "+str2[0]+str1[1]+str2[2:])

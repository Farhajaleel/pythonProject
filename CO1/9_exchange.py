# Create a string from given string where first and last charecters exchanged

str = input("Enter a string:")
new_str = str[-1] + str[1:-1] + str[0]
print("the string after exchange first and last charecters: ", new_str.strip())

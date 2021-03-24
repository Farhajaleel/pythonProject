# Get a string from an input string where all occurance  of first charecter replaced with '$' sxcept first charecter

user_str = input("Enter a string:")
first_char = user_str[0]
print("formatted string is: ", first_char + user_str.replace(first_char, "$")[1:])

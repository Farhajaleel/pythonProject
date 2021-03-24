# Add the 'ing' at the end of the given string, if it already ends with 'ing',then add 'ly'

str = input("Enter a string:")
if str.endswith("ing"):
    str += "ly"
else:
    str += "ing"
print("modified string is:", str)

# accept a filename from user and print extension of that

file = input("Enter a file name with extension:")
print("Extension of the filename is:", file.split(".")[-1])

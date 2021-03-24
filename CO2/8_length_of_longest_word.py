# Accept a list of words and return length of longest word

word_str = input("Enter some words seperated by commas:")
word_lst = word_str.split(",")
longest = len(word_lst[1])
for i in word_lst:
    if len(i) > longest:
        longest = len(i)
print("Length of logest word in the list is:", longest)

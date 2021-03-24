# Count the occurance of each word in a line of text

text="java language is a simple and powerfull programming language "
for i in text.strip().split():
    print("Number of occurence of word ","\"",i,"\""," is :",text.strip().split().count(i))


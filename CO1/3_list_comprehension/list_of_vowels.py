# form a list of vowels selected from a given word

word = input("Enter a word:")
vowel = [i for i in word if i in ['a', 'e', 'i', 'o', 'u']]
print(vowel)

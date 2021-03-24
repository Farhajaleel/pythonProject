# merge two dictionaries

dict1 = {
    "name": "john",
    "age": 25,
    "place": "vatakara"
}

dict2 = {
    "qualification": "degree",
    "email": "john@gmail.com"
}
print("Dictionaries before merge:\n\t", dict1, "\n\t", dict2)
dict1.update(dict2)
print("Dictionary items after merging:\n\t ", dict1)

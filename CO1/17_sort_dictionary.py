# Sort dictionary in ascending and descending order

student = {
    "name": "jazz",
    "age": 21,
    "place": "vatakara"
}

print("Ascending order:", sorted(student.items()))
print("Descending order:", sorted(student.items(), reverse=True))

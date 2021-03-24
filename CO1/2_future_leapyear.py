# Display future leap year from current year to a finel year entered by user

currentYear = 2020
futureYear = int(input("Enter a future year:"))
for i in range(currentYear, futureYear + 1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i)

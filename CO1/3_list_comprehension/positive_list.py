#generate positive list of numbers from a given list of integers

list=[10,0,-15,-27,35,-1,48,79,-24]
plist=[x for x in list if x > 0]
print(plist)
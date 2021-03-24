# printout all colors from color list 1 not contained in color list 2

color_list_1 = ["red", "black", "green", "yellow", "silver", "orange"]
color_list_2 = ["blue", "white", "silver", "gold", "grey", "black"]
print("Color list 1:", color_list_1)
print("Color list 2:", color_list_2)
print("Colors for list 1 not contained in list 2:", [i for i in color_list_1 if i not in color_list_2])

color_list1=input("enter color list1 seprated by space: ").split()
color_list2=input("enter color lis2: ").split()
unique_colors=[color for color in color_list1 if color not in color_list2]
print("color in list 1 not in list 2",unique_colors)


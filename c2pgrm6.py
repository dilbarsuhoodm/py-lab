list1=[int(x) for x in input ("enter the first list of integers:").split()]
list2=[int(x) for x in input ("enter the second list of integers:").split()]
same_length=len(list1)==len(list2)
same_sum=sum(list1)==sum(list2)
common_element=set(list1)&set(list2)
print("same length:",same_length)



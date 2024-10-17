number=[int(x) for x in input ("enter a list of integers(space=seprated):").split()]
odd_numbers = [num for num in number if num % 2 != 0]
print("list after removing even numbers",odd_numbers)

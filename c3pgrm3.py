def sum_of_list(lst):
    total = 0
    for item in lst:
        total += item
    return total  # This should be outside the for loop

number = [1, 2, 3, 4, 5]
print(f"Sum of the list is: {sum_of_list(number)}")


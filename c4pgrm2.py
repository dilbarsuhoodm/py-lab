def is_even(num):
    return num % 2 == 0

def check_number(num):
    if is_even(num):
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
result = check_number(number)
print(result)

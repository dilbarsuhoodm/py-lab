def calculating_simple_interest(principle, time, is_senior):
    rate = 12 if is_senior else 10
    SI = (principle * rate * time)/100
    return SI
principle = float(input("enter the principal amount: "))
time = float(input("enter the time in years: "))
is_senior = input("is the customer a senior citizen? (yes/no): ").strip().lower() == "yes"

interest = calculating_simple_interest(principle, time, is_senior)
print("The simple interest is:", interest)

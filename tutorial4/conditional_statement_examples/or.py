print("Enter integer 1:")
number1 = int(input())

print("Enter integer 2:")
number2 = int(input())

print("Enter integer 3:")
number3 = int(input())

if number1 != number2 or number2 != number3:  # "!=" means not equal.
    print("You did not enter 3 identical integers.")
else:
    print("These three integers are equal.")

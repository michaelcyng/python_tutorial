print("Enter integer 1:")
number1 = int(input())

print("Enter integer 2:")
number2 = int(input())

print("Enter integer 3:")
number3 = int(input())

if number1 == number2 and number2 == number3: # "==" means equal. Notice the difference between "=" and "=="
    print("These three integers are equal.")
else:
    print("You did not enter 3 identical integers.")

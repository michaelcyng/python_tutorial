print("Input an integer below:")
number = int(input())
remainder = number % 2
is_odd = (remainder == 1)

if is_odd:
    print("The integer is odd.")
else:
    print("The integer is even.")

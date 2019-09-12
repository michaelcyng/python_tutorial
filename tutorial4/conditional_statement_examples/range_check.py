print("Input an integer below:")
number = int(input())

if 0 <= number <= 10:
    # A number x is within the closed interval [a, b] if a <= x <= b
    print("This number is within the closed interval [0, 10]")
elif number < 0:
    print("This is a negative number")
else:
    print("This number is greater than 10")

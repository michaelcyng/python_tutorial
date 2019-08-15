print("Input an integer below:")
number = int(input())

if number > 0:
    print("The number is positive")
elif number < 0:  # if number is not greater than 0, we firstly check this one
    print("The number is negative")
else:  # if number is neither greater than 0 nor less than 0, we run the below statement
    print("The number is 0")

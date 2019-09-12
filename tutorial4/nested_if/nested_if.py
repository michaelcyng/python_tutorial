print("Input an integer:")
number = int(input())

if number > 0:
    print("The integer is positive")
    if number % 2 == 0:  # another if inside if
        print("The integer is also even.")
    else:
        print("The integer is also odd.")
else:
    print("The integer is not positive")

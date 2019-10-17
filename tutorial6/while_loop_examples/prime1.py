print("Please enter a positive integer")
number = int(input())

is_prime = (number > 1)
factor = 2
while factor < number:  # The following runs as long as this condition is true
    if number % factor == 0:
        is_prime = False
        break
    factor += 1

if is_prime:
    print("{0} is a prime number.".format(number))
else:
    print("{0} is not a prime number.".format(number))

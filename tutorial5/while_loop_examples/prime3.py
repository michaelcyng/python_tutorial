print("Please enter a positive integer")
number = int(input())

is_prime = (number == 2) or ((number > 1) and (number % 2 != 0))
factor = 3
while is_prime and (factor * factor <= number):  # The following runs as long as this condition is true
    is_prime = (number % factor != 0)
    factor += 2

if is_prime:
    print("{0} is a prime number.".format(number))
else:
    print("{0} is not a prime number.".format(number))

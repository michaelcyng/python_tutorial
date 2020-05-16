from math_utility.prime import is_prime

print('Input an integer: ', end='')
number = int(input())

if is_prime(number):
    print('The integer is prime')
else:
    print('The integer is not prime')

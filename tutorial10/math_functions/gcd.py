from math import gcd

print("Input an integer: ", end='')
integer1 = int(input())

print("Input another integer: ", end='')
integer2 = int(input())

print(f'The greatest common divisor of {integer1} and {integer2} is {gcd(integer1, integer2)}.')

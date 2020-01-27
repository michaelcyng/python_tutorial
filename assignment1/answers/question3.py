print("Enter the value of n:")
n = int(input())

total = 0  # This value holds the sum of the values inputted so far
index = 1
while index <= n:
    new_value = index
    total += new_value
    index += 1

print("The sum is {0}".format(total))

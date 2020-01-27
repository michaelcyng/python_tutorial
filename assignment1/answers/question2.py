
print("Enter the value of n:")
n = int(input())

total = 0  # This value holds the sum of the values inputted so far
index = 0
while index < n:
    print("Enter integer {0}:".format(index))
    new_value = int(input())
    total += new_value
    index += 1

print("The average is {0}".format(total / n))

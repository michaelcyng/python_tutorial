print("Please enter a positive integer: ")
required_count = int(input())
count = 1

print("Start counting")
while count <= required_count:  # The following runs as long as this condition is true
    if count % 2 == 0:
        print("{0} is an even integer".format(count))
    else:
        print("{0} is an odd integer".format(count))
    count += 1
print("Counting ended")

print("Please enter a positive integer")
required_count = int(input())
count = 1

# required_count = 3
# count = 4

# Display:
# Count: 1
# Count: 2
# Count: 3

print("Start counting")
while count <= required_count:  # The following runs as long as this condition is true
    print("Count: {0}".format(count))
    count += 1  # count = count + 1

print("Please enter a positive integer")
required_count = int(input())
count = 1

print("Start counting")
while count <= required_count:  # The following runs as long as this condition is true
    print("Count: {0}".format(count))
    count += 1
    if count > 5:
        print("Count is greater than 5. Exit the loop")
        break
print("Left the loop")

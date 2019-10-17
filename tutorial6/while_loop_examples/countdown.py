print("Please enter a positive integer: ")
count = int(input())

print("Start counting down")
while count >= 0:  # The following runs as long as this condition is true
    print("Count: {0}".format(count))
    count -= 1
print("Counting ended")

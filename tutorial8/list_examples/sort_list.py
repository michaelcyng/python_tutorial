print("Give me five numbers")

numbers = []
index = 0
while index < 5:
    numbers.append(int(input()))
    index += 1

print(sorted(numbers))

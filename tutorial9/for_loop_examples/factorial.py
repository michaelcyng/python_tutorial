print("Input a non-negative integer: ")
input_value = int(input())

result = 1
for number in range(input_value):
    result *= number

print(result)

print("Input a non-negative integer: ")
input_value = int(input())

result = 1
for number in range(1, input_value + 1):
    result *= number

print(result)

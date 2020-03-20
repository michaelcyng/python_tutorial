print("Enter the number of rows:")
num_rows = int(input())

print("Enter the number of columns:")
num_columns = int(input())

for _ in range(num_rows):
    for _ in range(num_columns):
        print("*", end="")  # end="" means after printing the string, it will not go to the new line
    print("")

def draw_line(num_columns):
    for _ in range(num_columns):
        print("*", end="")
    print("")


print("Enter the number of rows:")
num_rows = int(input())

print("Enter the number of columns:")
num_columns = int(input())

for _ in range(num_rows):
    draw_line(num_columns)

def draw_line(num_columns=3):
    for _ in range(num_columns):
        print("*", end="")
    print("")


print("Enter the number of rows:")
num_rows = int(input())

for _ in range(num_rows):
    draw_line()

from utility import draw_line


print("Enter the number of rows:")
num_rows = int(input())

print("Enter the number of columns:")
num_columns = int(input())

for _ in range(num_rows):
    draw_line(num_columns)

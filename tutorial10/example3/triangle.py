from utility.draw import draw_line


print("Enter the number of rows:")
num_rows = int(input())

for row in range(1, num_rows + 1):
    draw_line(row)

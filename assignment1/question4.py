# TODO:
# 1. Try to guess what this program aims to do
# 2. Run this program to verify if your anticipation is correct
# 3. Modify the program as follows:
#    a) Only requires the input of the number of rows
#    b) For the i-th row, print out i asterisks, for example,
#       if there are 5 rows, print out the following:
#       *
#       **
#       ***
#       ****
#       *****

print("Enter the number of rows:")
num_rows = int(input())
print("Enter the number of columns:")
num_columns = int(input())

row_index = 0
while row_index < num_rows:
    column_index = 0
    while column_index < num_columns:
        print("*", end="")
        column_index += 1
    print()
    row_index += 1

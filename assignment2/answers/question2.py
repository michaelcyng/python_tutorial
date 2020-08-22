# Source: https://leetcode.com/problems/shuffle-the-array/
#
# Given the value of n and a list of 2n integers denoted by nums = [x0, x1, ..., x{n - 1}, y0, y1, ..., y{n - 1}],
# complete the following program to generate a list shuffled_list = [x0, y0, x1, y1, ..., x{n - 1}, y{n - 1}]
#
# Example 1:
#              index =[0, 1, 2 , 3, 4, 5]
# If n = 3 and nums = [2, 5, 1 | 3, 4, 7], shuffled_list = [2, 3, 5, 4, 1, 7]
# left_index = 0, 1, 2
# right_index = 3, 4, 5
# left_index => 0, 1, ..., n - 1
# right_index = n + left_index
#
# Example 2:
# If n = 4 and nums = [1, 2, 3, 4, 4, 3, 2, 1], shuffled_list = [1, 4, 2, 3, 3, 2, 4, 1]
#
# Example 3:
# If n = 2 and nums = [1, 1, 2, 2], shuffled_list = [1, 2, 1, 2]

print("Input the value of n: ", end="")
n = int(input())
nums = list()
for _ in range(2 * n):
    print("Input an integer: ", end="")
    number = int(input())
    nums.append(number)

# TODO: Replace here with the code which generates shuffled_list from nums
shuffled_list = list()
for left_index in range(n):
    right_index = n + left_index
    shuffled_list.append(nums[left_index])
    shuffled_list.append(nums[right_index])


print("The corresponding shuffled_list is {}".format(shuffled_list))

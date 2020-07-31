# Source: https://leetcode.com/problems/running-sum-of-1d-array/
#
# Given a list "nums", complete the following program computes the corresponding list of running sum "run_sum".
# Running sum is defined as run_sum[i] = nums[0] + nums[1] + ... + nums[i]
#
# Example 1:
# If nums = [1, 2, 3, 4], run_sum = [1, 3, 6, 10]
#
# Example 2:
# If nums = [1, 1, 1, 1], run_sum = [1, 2, 3, 4]
#
# Example 3:
# If nums = [3, 1, 2, 10, 1], run_sum = [3, 4, 6, 16, 17]
#

print("Input the number of integers: ", end="")
num_integers = int(input())
nums = list()
for _ in range(num_integers):
    print("Input an integer: ", end="")
    number = int(input())
    nums.append(number)

run_sum = [nums[0]]
for num in nums[1:]:
    run_sum.append(num + run_sum[-1])

print("The list of running sum is {}".format(run_sum))

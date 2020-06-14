# Source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
#
# You are given a integer list called candies, where candies[i] means the number of candies the i-th child has.
# You are also given an integer x, which is the extra number of candies that you can distribute to the children.
# For a given j (start with 0), complete the following program which determines whether there is a way to distribute
# those x candies to the children so that the j-th child has the greatest number of candies. Provide the answer as a
# boolean variable can_be_greatest.
#
# Example 1:
# If candies = [2, 3, 5, 1, 3], x = 3 and j = 1, can_be_greatest = True because if we distribute 2 candies to the
# child 1, he/she will have 3 + 2 = 5 candies. Then, if we do not distribute the 1 remaining candy to child 2, who has
# already got 5 candies, he is one of the children having the greatest number of candies
#
# Example 2:
# Consider the same values for candies and x as in example 1 but now, j = 4, can_be_greatest = False because even if
# you give all 3 candies to child 4, he/she can have at most 1 + 3 = 4 candies, which is fewer than what child 2 has.

print("Input the number of children: ", end="")
num_children = int(input())

candies = list()
for child in range(num_children):
    print("Input the number of candies of child {}".format(child))
    num_candies = int(input())
    candies.append(num_candies)

print("Input the number of extra candies: ", end="")
x = int(input())

print("Input the value of j: ", end="")
j = int(input())

# TODO: Determine whether we can distribute the x candies to the children so that child j can have the greatest number
#       of candies. Provide the answer with the boolean variable can_be_greatest

if can_be_greatest:
    print("Child {} can have the greatest number of candies.".format(j))
else:
    print("Child {} still cannot have the greatest number of candies.".format(j))

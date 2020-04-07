def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("Input the value of n: ", end="")
n = int(input())
print("n! = {}".format(factorial(n)))

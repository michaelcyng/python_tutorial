def is_divisible(dividend, divisor):
    return (dividend % divisor) == 0


def is_prime(number):
    if number == 1:
        return False

    for factor in range(2, number - 1):
        if is_divisible(number, factor):
            return False
    return True

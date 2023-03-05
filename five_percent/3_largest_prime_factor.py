import math


def find_least_divisor(target):
    """
    Returns [prime_number_divisor, quotient]
    If prime_number_divisor is 0, quotient is prime number
    """
    target_square_root = int(math.ceil(math.sqrt(target)))
    for i in range(2, target_square_root):
        if target % i == 0:
            return [i, int(target / i)]
    return [0, target]


if __name__ == '__main__':
    print("Problem 3 - Largest Prime Factor")
    target = 600851475143
    # target = 13195
    curr = [1, target]
    largest_prime_factor = 1
    run = True
    while run:
        curr = find_least_divisor(curr[1])
        print("curr: [" + str(curr[0]) + ", " + str(curr[1]) + "]")
        if curr[0] > largest_prime_factor:
            largest_prime_factor = curr[0]
        if curr[0] == 0:
            largest_prime_factor = curr[1]
            run = False

    print("largest prime number", largest_prime_factor)

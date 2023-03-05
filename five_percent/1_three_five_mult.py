def is_mult(n):
    return n % 3 == 0 or n % 5 == 0


if __name__ == '__main__':
    result = 0
    for i in range(1, 1000):
        if (is_mult(i)):
            result += i
    print("result: " + str(result))

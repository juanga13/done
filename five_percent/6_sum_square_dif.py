if __name__ == '__main__':
    print("Problem 6 - Sum square difference")
    limit = 100
    # sum of squares
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, limit + 1):
        square_i = i ** 2
        sum_of_squares += square_i
        square_of_sum += i
    square_of_sum = square_of_sum ** 2

    diff = square_of_sum - sum_of_squares

    print(diff)

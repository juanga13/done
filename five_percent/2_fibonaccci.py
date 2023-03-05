def is_even(n):
    return n % 2 == 0


if __name__ == '__main__':
    limit = 4 * 1000 * 1000
    saved_fib = [0, 1]

    # create array of fib elem until 4M
    while saved_fib[len(saved_fib) - 1] <= limit:
        prev = saved_fib[len(saved_fib) - 1]
        prev_prev = saved_fib[len(saved_fib) - 2]
        new_fib = prev + prev_prev
        saved_fib.append(new_fib)
        print("[" + str(prev) + ", " + str(new_fib) + "]")

    # iterate array and sum every even
    result = 0
    for fib_elem in saved_fib:
        print("* " + str(fib_elem))
        if (is_even(fib_elem)):
            result += fib_elem

    print(result)

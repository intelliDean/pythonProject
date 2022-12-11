def loop_with_if():
    sum_of_evens = 0
    for n in range(1, 100):
        if n % 2 == 0:
            sum_of_evens += n
            print(sum_of_evens, end=" ")
            if n % 10 == 0:
                print()


if __name__ == '__main__':
    loop_with_if()

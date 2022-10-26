def break_loop():
    for n in range(0, 4):
        if n == 2:
            break
        print(n)
    print(f"Finished with n = {n}")


if __name__ == '__main__':
    break_loop()

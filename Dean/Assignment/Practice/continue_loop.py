def continue_loop():
    for i in range(0, 4):
        if i == 2:
            continue  # skipped n = 2 but cexecutes the code after 2
        print(i)
    print(f"Finished with i = {i}")


if __name__ == '__main__':
    continue_loop()

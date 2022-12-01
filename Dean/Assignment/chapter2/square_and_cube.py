def square_and_cube():
    print("""Number   Squares    Cubes""")
    for i in range(1, 11):
        square = i * i
        cube = i * i * i
        print(f"{i} {square:10}{cube:11 }")


if __name__ == '__main__':
    square_and_cube()
def palindromes(pal):
    rev = reversed(pal)
    if rev == pal:
        print(rev)
    else:
        print(pal)


if __name__ == '__main__':
    enter = input("enter string\n")
    palindromes(enter)

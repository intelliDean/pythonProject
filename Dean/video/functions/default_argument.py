def greeting(name, greet="Good day"):  # if greeting argument is not supplied, the default greeting is Good day but if
    # supplied, it overrides the default. The default will be the last parameter set
    return greet+" "+name


if __name__ == '__main__':
    print(greeting("Dean", "Good afternoon"))
    print(greeting("Mike"))



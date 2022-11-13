def conc():
    make = ['a', 'b', 'c']
    take = ['A', 'B', 'C']
    fake = make[0:]+take[0:]
    return fake


if __name__ == '__main__':
    done = conc()
    print(done)

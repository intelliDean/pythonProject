def position(lists: list[str]) -> list:
    return list(enumerate(lists))


if __name__ == '__main__':
    pref = ['apple', 'banana', 'pineapple', 'mango', 'pawpaw', 'cashew']
    print(position(lists=pref))

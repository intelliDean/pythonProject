def loop(item_list: list) -> None:
    for item in item_list:
        print("fruit", item)


def loop_and_enumerate(item_list: list) -> None:
    for item in enumerate(item_list):
        print("colour", item[1], item[0])
        # when enumerate returns, it returns a list of tuples,
        # i.e, a tuple with pair of each element index and the element itself
        # with the index at 0 index and the element at index 1


if __name__ == '__main__':
    fruits = ['orange', 'pineapple', 'pawpaw', 'apple']
    colours = ['pink', 'red', 'orange', 'black']

    loop(item_list=fruits)
    print("\n")
    loop_and_enumerate(item_list=colours)

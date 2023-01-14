def create_list(list_size: int) -> list:
    item_list = []
    for i in range(0, list_size):
        item_list.append(input(f"enter the item in {i} index\n-> "))
    return item_list


if __name__ == '__main__':
    print(create_list(5))

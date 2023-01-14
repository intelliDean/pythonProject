def add_to_list(no_of_items: int, item: str) -> None:
    item_list = []
    for i in range(no_of_items):
        item_list.append(item)
        print(item_list[i])


if __name__ == '__main__':
    add_to_list(no_of_items=7, item='Jesus is Lord')
    

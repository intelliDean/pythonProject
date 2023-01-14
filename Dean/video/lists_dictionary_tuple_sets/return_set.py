from typing import Set, Any


def unique_items(items: list) -> set[Any]:  # normal function to return a set
    return set(items)


unique_numbers = lambda lists: list(set(lists))  # lambda to return a list

if __name__ == '__main__':
    items_ = [1, 2, 3, 2, 3, 43, 2, 43, 2, 3, 1]
    print(unique_items(items=items_))

    print(unique_numbers(items_))
 
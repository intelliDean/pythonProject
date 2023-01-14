def tuple_unpacking(items: list) -> None:
    for index, item in enumerate(items):
        print(f'Item {(index + 1)}: {item}')


if __name__ == '__main__':
    fruits = ['orange', 'pineapple', 'pawpaw', 'apple']
    tuple_unpacking(fruits)

    fruits.append('mango')
    fruits.append('water melon')
    fruits.insert(4, 'cherry')
    print()
    tuple_unpacking(fruits)

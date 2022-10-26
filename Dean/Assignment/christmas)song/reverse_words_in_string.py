if __name__ == '__main__':
    my_string = 'This is big brother'
    string_elements = my_string.split()
    reversed_elements = []
    for elements in string_elements:
        reversed_elements.append(elements[::-1])
    print(reversed_elements)

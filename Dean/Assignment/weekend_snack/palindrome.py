def palindrome(lists):
    new_list = []
    for i in reversed(lists):
        new_list.append(i)
    if new_list == lists:
        return True
    else:
        return False


if __name__ == '__main__':
    rays = ['m', 'a', 'd', 'a']
    result = palindrome(rays)
    print(result)

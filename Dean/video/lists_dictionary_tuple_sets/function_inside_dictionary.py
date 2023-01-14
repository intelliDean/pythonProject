def meet_me(dic: dict) -> str:
    # a list in a dictionary and a function call inside a dictionary
    return f"""
    Hi, my name is {dic['name']} and I am {dic['age']}
    I live in the city of {dic['city']}, in my multi-billion dollars {dic['house']} 
    I drive {dic['cars']}
    My networth is ${dic['net_worth']():,} USD"""


if __name__ == '__main__':
    dean = {
        'name': 'Michael Dean Oyewole',
        'age': 23,
        'cars': ['Bra-Bus', 'Lamborghini', 'Porsche', 'Aston Martin', 'Rolls Royce'],
        'house': 'Mansion',
        'city': 'Lagos',
        'asserts': 540000000,
        'debt': 3400,
        'net_worth': lambda: dean['asserts'] - dean['debt']  # a lambda function inside a diction
    }
    print(list(dean.values())[7]())
    print(list(dean.values()))

    print(meet_me(dean))

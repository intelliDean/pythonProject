def introduction(dictionary: dict) -> str:
    return f"""
    Hello everyone and welcome to the 2023 edition of Forbes.
    I have the honour to introduce to you the richest man in the world.
    Here is a little introduction of him.
    His name is {dictionary['name']} and he is a {dictionary['job']},
    He made his first billion dollars at {dictionary['age']}
    He is the first {dictionary['complexion']} man to make this achievement
    """


if __name__ == '__main__':
    dean = {
        'name': 'Michael Dean',
        'age': 23,
        'phone_number': '08095729090',
        'complexion': 'Black',
        'job': 'Software Engineer'}
    print(introduction(dean))

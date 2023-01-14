numbers = 10, 10, 10
lst = list(numbers)

print(lst)
lst.append(23)
print(lst[-1])

dean = {
    'name': 'Michael Dean',
    'Age': 23,
    'phone_number': '08095729090',
    'complexion': 'Black',
    'love_language': 'Words of Affirmation'}

print(dean)

dean['laptop'] = 'HP'

print(dean)

print(dean['phone_number'])
amount = int(dean['phone_number'])

new_amount = 500 + amount
print(new_amount)

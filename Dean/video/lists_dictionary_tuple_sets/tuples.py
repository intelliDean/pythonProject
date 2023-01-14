fruits = 'mango', 'banana', 'grapes', 'oranges', 'pineapple'

print(fruits)
print(fruits[0])

list(fruits)[0] = 'water melon'
new_fruits = list(fruits)

new_fruits[0] = 'water melon'

print(list(fruits))  # it did not change the elements in the tuples

new_tuple = tuple(new_fruits)  # this is the new tuple converted from list
print(new_tuple)
print(new_fruits)

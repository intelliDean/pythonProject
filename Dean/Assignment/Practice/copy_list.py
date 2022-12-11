animals = ["Lion", "Tiger", "Bandersnatch"]  # slicing method
large_cats = animals[:]  # with the square bracket and colon, both variables won't be pointing at the s object in
# memory, instead, animals will copy into large_cats from beginning to the end
large_cats.append("Leopard")

number1 = 1, 2, 3, 4, 5, 6
number2 = number1[:]

nested_list1 = [[200, 320, 120, 700], [120, 450, 500]]
copied_nested_list = nested_list1[:]
copied_nested_list.append([230, 150, 600])

copied_nested_list.sort(key=len)

print(copied_nested_list)

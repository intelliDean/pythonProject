print("line 1\n", format(0.0032, "10.2%"))

print("line 2\n", format(50097.467657, "<10.2f"), format(23993.43, "<10.2f"), format(566.0999, "<10.2f"))

print("line 3\n", format(59832, "10d"))
print("line 4\n", format(59832, "<10d"))
print("line 5\n", format(59832, "10x"))
print("line 6\n", format(59832, "<10x"))


print(format("Welcome to Python", "20s"))
print(format("Welcome to Python", "<20s"))
print(format("Welcome to Python", ">20s"))
print(format("Welcome to Python and Java", ">20s"))

input_file = open("temp.txt", "r")
output_file = open("output.txt", "w")
for line_str in input_file:
    new_str = ''
    line_str = line_str.strip()
    for char in line_str:
        new_str = char + new_str
        print(new_str, file=output_file)
        print('Line: {:12s} reversed is: {:s}'.format(line_str, new_str))
input_file.close()
output_file.close()


temp_file = open("temp.txt", "w")
print("first line", file=temp_file)
print("second line", file=temp_file)
temp_file.close()
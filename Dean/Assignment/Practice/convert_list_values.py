def convert_string_list_to_float(str_values):
    float_values = [float(value) for value in str_values]
    return float_values


if __name__ == '__main__':
    str_values = ["1.5", "9.3", "6.2", "3.92"]
    flo = convert_string_list_to_float(str_values)
    print(flo)

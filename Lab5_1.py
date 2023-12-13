def find_max_value(my_list):
    max_value = max(my_list)
    return max_value if max_value > 0 else "Число менше 0"

my_list = [3, -5, 11, 7, 4, -3]
result = find_max_value(my_list)
print(result)

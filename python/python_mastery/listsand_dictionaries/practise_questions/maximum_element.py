def maximum_number(list):
    sorted_list = sorted(list, reverse=True)
    maximum_number = sorted_list[0]
    return maximum_number


print(maximum_number([1, 5, 6, 9, 0, 10, 1]))
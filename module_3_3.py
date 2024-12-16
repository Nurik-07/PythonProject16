def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [12, 23, 34]
values_dict = {"a":45, "b":56, "c":67}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [78, 89]
print_params(*values_list2, 90)









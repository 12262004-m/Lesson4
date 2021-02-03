my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for i, j in enumerate(my_list):
    if my_list[i-1] < my_list[i]:
        new_list.append(j)
print(new_list [1: ])

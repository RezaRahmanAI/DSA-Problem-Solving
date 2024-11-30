def reverse_list(list):
    reversed_list = []
    for i in range(len(list) -1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list


my_list = [2,3,4,5]
reversed_list = reverse_list(my_list)

print(reversed_list)

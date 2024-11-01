i = -1
while True:
    i = i + 1
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    if my_list[i] == 0:
        continue
    if my_list[i] > 0:
        print(my_list[i])
    else:
        break

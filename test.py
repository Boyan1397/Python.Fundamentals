my_list = ["cat","dog","parrot"]
while my_list:
    print(my_list[0],end=" ")
    current_element = my_list[0]
    my_list.remove(current_element)
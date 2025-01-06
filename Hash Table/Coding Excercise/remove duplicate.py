def remove_duplicates(my_list):
    my_set = set()
    new_list = []
    
    for num in my_list:
        if not num in my_set:
            my_set.add(num)
            new_list.append(num)
    
    return new_list
    


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    (Order may be different as sets are unordered)

"""
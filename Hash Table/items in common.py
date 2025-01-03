def items_in_common(list1, list2):
    dict = {}

    for nums in list1:
        dict[nums] = True
    
    for nums in list2:
        if nums in dict:
            return True
    
    return False


print(items_in_common([1,3,5], [2,4,6]))
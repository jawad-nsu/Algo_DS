def group_anagrams(arr_str):
    dict = {}
    res = []
    for i in range(len(arr_str)):
        sorted_arr = ''.join(sorted(arr_str[i]))
        
        if sorted_arr in dict:
            dict[sorted_arr].append(arr_str[i])
        else:
            dict[sorted_arr] = [arr_str[i]]
        
    for key, value in dict.items():
        res.append(value)
    
    return res
        
    
    




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
def first_non_repeating_char(str):
    dict = {}
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] = False
        else:
            dict[str[i]] = True
    
    for i in range(len(str)):
        if dict[str[i]] == True:
            return str[i]
    
    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
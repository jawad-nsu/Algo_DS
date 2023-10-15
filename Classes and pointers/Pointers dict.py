dict1 = {'value': 11}
dict2 = dict1

# print('before dict2 is updated')
print('value of dict1: ', dict1)
print('value of dict2: ', dict2)
print('address of dict1: ', id(dict1))
print('address of dict2: ', id(dict2))

dict2['value'] = 22
print('\nafter updating dict2')
print('value of dict1: ', dict1)
print('value of dict2: ', dict2)
print('address of dict1: ', id(dict1))
print('address of dict2: ', id(dict2))

dict3 = {'value': 33}
dict2 = dict3
print('\nvalue of dict2: ', dict2)
print('address of dict2: ', id(dict2))
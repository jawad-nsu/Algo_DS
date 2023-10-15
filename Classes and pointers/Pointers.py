num1 = 11
num2 = num1

print('Before the value of num2 is updated')
print('value of num1: ', num1)
print('value of num2: ', num2)

print('address of num1: ', id(num1))
print('address of num2: ', id(num2))

num2 = 22
print('\nafter num2 is updated')
print('value of num1: ', num1)
print('value of num2: ', num2)

print('address of num1: ', id(num1))
print('address of num2: ', id(num2))
# time complexity, O(n+n) = O(n)
def print_items(n):
    for i in range(n):
        print(n)
    for j in range(n):
        print(n)
        
# time complexity, O(a+b)
def print_items(a, b):
    for i in range(a):
        print(a)
    for j in range(b):
        print(b)

# time complexity, O(n * n) = O(n²)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# time complexity, O(a * b) = O(a * b)
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)
    
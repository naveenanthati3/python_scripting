def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# directly pass literal values
print_max(1, 1)

x = 22
y = 22

# pass variables as arguments
print_max(x, y)

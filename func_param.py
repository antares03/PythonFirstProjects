def printMax(a, b):
    if a > b:
        print('a =',a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

printMax(8, 4) # directly pass literal values

x = 5
y = 7

printMax(x, y) # pass variables as arguments

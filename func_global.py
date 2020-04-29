x = 50

def func():
    global x

    print('x is equal' , x)
    x = 2
    print('change global value x to', x)

func()
print('Value of x is', x)

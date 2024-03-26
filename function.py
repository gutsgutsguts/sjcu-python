def hello():
    print("Hello World")
    
hello()

def add(x, y):
    print(x)
    print(y)
    return x + y

val_x = 1
val_y = 2

val_sum = add(val_x, val_y)
print(val_sum)

print(add(y=val_y, x= val_x))

def add(x, y = 10):
    print(x)
    print(y)
    return x + y

print(add(1,2))
print(add(1))

def sum(*values):
    result = 0
    for one in values:
        result = result + one
    return result

result = sum(1, 2, 3)
print(result)

def calc(a, b):
    return a + b, a - b

result = calc(1,3)
print(result)

x, y = calc(1,3)
print(x)
print(y)
# 내장함수 임포트 할 필요없음

# 절대값
print(abs(-7))

print(all([1,2,3,4,5,6,7,8,9,10]))
print(all([1,2,3,4,5,6,7,8,9,0]))
print(any([1,2,3,4,5,6,7,8,9,0]))

print(dir([1,2]))
print(dir({'chirs' : 1, 'tommy' : 2}))

print(divmod(5,2))

for index, name in enumerate(['chris', 'tommy', 'harry']):
    print(index, name)
    
print(eval('1+4/2'))

data = list("Hello World")
print(data)

def multiple(x):
    return x*2

data = list(map(multiple, [1,2,3,4,5]))
print(data)

print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))

print(round(7.7))

data = sorted("Hello World")
print(data)

print(type(data))

data = list(zip([1,2,3], ['a', 'b', 'c']))
print(data)


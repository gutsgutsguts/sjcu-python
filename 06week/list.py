# 리스트 자료구조의 특징과 기본적인 사용법

var = [1,'chris',['tommy','harry'],('hans', 2)]
print(var)
print(var[3])
print(var[3][0])
print(var[-1])

print(var)



#리스트 연산
x = [1,2,3]
y = [3,5,6]
var = x + y
print(var)

var = x * 2
print(var)

var = [1,2,3]
var.append(4)
print(var)

var.extend([10,11,12])

var.insert(0,0)
print(var)

var = var * 2
print(var)
var.remove(4)
print(var)

print(var.count(2))

# print(var.index(5))
try:
    print(var.index(5))
except ValueError:
    print('ValuError')
    
import random
var = list()
for i in range(10):
    var.append(random.randint(1, 100))
print(var)

var.sort()
print(var)

var.reverse()
print(var)

var.clear
print(var)

var = []
 
for data in range(1, 11):
    if data % 2 == 0:
        var.append(data)
print(var)

var = list(filter(lambda x : x % 2 == 0, range(11)))
print(var)

var = [data for data in range(1, 11) if data % 2 == 0]
print(var)

var = [(x, y) for x in range(1, 11) for y in range(1, 11) if x + y == 10]
print(var)

var = [x for x in range(1, 11) if x % 2 == 0 if 5 < x]
print(var)

var = (data + 10 for data in range(1,11) if data % 2 == 0)
print(var)

var = (data + 10 for data in range(1, 11) if data % 2 == 0)
print(var)

try:
    print(next(var))
    print(next(var))
    print(next(var))
    print(next(var))
    
    print(next(var))
except StopIteration:
    print("StopIteration")
    
stack = [1,2,3]
stack.append(4)
stack.append(5)
print(stack)

var = stack.pop()
print(var)
print(stack)

var = stack.pop()
print(var)
print(var)

from collections import deque
queue = deque(["chris", "tommy", "harry"])
queue.append("hans")
print(queue)

var = queue.popleft()
print(var)
print(queue)


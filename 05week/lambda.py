add = lambda a, b : a + b
result = add(1,3)
print(result)

result = (lambda a, b : a + b)(1,4)
print(result)

result = (lambda a, b : a + b)(a=2,b=4)
print(result)

result = lambda a, b = 4: a + b(1)
print(result) 

print((lambda a, b : a if a%2 == 0 else b)(1,3))

print((lambda a, b : '{} + {} = {}'.format(a,a,a+b)) (1, 5))

data = ['Python Lambda', 'Python', 'Hello World' ]
data.sort(key=lambda x: len(x))
print(data)

data = list(map(lambda x: x*2, range(10)))
print(data)

data = list(filter(lambda x: x % 2 == 0, range(10)))
print(data)

def calc(op):
    if op == '+':
        return lambda a, b : a + b
    elif op == '-':
        return lambda a, b : a - b
    elif op == '/':
        return lambda a, b : a / b
    elif op == '*':
        return lambda a, b : a * b
    else:
        return lambda a, b : a % b

myCalc = calc('+')
print(myCalc(1,6))         


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

fac = lambda n : 1 if n == 1 else n * fac(n - 1)
print(fac(5))

import threading
import time

def thread_main(x):
    print(f'{x} - thread satrt')
    time.sleep(1)
    print(f'{x} - thread end')
    
print('---thread start---')
thread_main(0)
thread_main(1)
thread_main(2)
thread_main(3)
thread_main(4)
thread_main(5)
thread_main(6)
thread_main(7)
thread_main(8)
thread_main(9)
print('---thread end---')

print('---multi thread start---')
threads = []
for i in range(10):
    t = threading.Thread(target=thread_main, args=(i,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
print('---multi thread end---')

number = 0
lock = threading.Lock()

def thread_counter(x):
    global number
    print(f'{x} - Thread start - {number}')
    lock.acquire()
    time.sleep(1)
    number += 1
    print(f'{x} - Thread end - {number}')
    lock.release()
    
print('----- Threads Start -----')
thread_counter(0)
thread_counter(1)
thread_counter(2)
thread_counter(3)
thread_counter(4)
thread_counter(5)
thread_counter(6)
thread_counter(7)
thread_counter(8)
thread_counter(9)
print('----- Threads End -----')

print('---multi thread start---')
number = 0
threads = []
for i in range(10):
    t = threading.Thread(target=thread_counter, args=(i,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
print('---multi thread end---')

class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 별명 입니다"
    
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
    
try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print("허용되지 않는 별명입니다.")
    
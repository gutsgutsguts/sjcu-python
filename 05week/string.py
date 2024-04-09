str = 'hello world'
print(type(str))

str = 'hello world'
print(len(str))

str = 'hello world'
print(str.count('l'))

str = 'hello My world'
print(str.find('My'))
print(str.find('Your'))

str = 'hello My world'
print(str.rfind('o'))

str = 'hello My world'
try:
    print(str.index('Your'))
except ValueError as e:
    print(e)

str = '-'.join('Hello')
print(str)

str = 'Hello World'
print(str.upper())

str = 'Hello World'
print(str.lower())

str = '   hello world    '
print(str.lstrip())

str = '     hello world     '
print(str.rstrip())

str = '    hello world    '
print(str.strip())

str = 'hello My world'
print(str.replace('My', 'Your'))

str = 'Hello My World'
print(str.split(' '))

str = 'Hello-your-world'
print(str.split('-', 1))

srt = 'Start'
print(str.zfill(10))

srt = 'Start'
print(str.rjust(10, '1'))

srt = 'Start'
print(str.ljust(10, '1'))

str = "Start"
print(str.center(10, '-'))

str = 'Hello World'
reversed_str = ''
for c in str:
    reversed_str = c + reversed_str
print(reversed_str)

str = 'Hello World'
str_list = list(str)
str_list.reverse()
reversed_str = ''.join(str_list)
print(reversed_str)

str = 'Hello World'
reversed_str = str[::-1]
print(reversed_str)
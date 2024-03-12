file = open("test.txt", "w")
for data in range(1, 11):
    file.write(f'{data} line');
file.close()

file = open("test.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close

file = open("test.txt", "a")
for data in range(1, 11):
    file.write(f'{data} line\n');
file.close()

file = open("test.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
file.close()

file = open("test.txt", "r")
data = file.read()
print(data)
file.close()

with open("test.txt", "r") as file:
    data = file.read()
    print(data)

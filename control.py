cond = True
if cond :
    print("Execute")
    
var = 10

if 0 < var:
    print("Big")
else:
    print("Small")
    

var = input("Enter a number: ")
var = int(var)

if 10 < var:
    print("Bigger than 10")
elif 5 < var:
    print("Bigger than 5")
elif 0 < var:
    print("Bigger than 0")
else:
    print("Too small")
    
x, y = 10, 20
if 0 < x and y < 30:
    print("Good")
else:
    print("Bad")
    

var = input("Enter a number: 0")
var = int(var)

if x !=var and y !=var:
    print("Bad")
else:
    print("Good")
    
    
var = [1, 2, 3]
print (1 in var)

var = ["chris", "tommy", "harry"]
print("chris" in var)

var = "Hello Python"
print("J" not in var)

var = input("Enter a number: ")
var = int(var)

var = "Big" if 10 < var else "small"
print(var)


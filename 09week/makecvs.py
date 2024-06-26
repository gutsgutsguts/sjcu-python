import random

def calcGrade(kor, math):
    mean = int((kor + math) / 2)
    grade = "C"
    
    if 70 <= mean:
        grade = "A"
    elif 40 <= mean:
        grade = "B"
        
    return grade

fp = open("grade.csv", "w", encoding="utf-8")
fp.write("KOR,MATH,GRADE\n")

for i in range(10000):
    kor = random.randint(10, 100)
    math = random.randint(10, 100)
    grade = calcGrade(kor, math)
    fp.write("{0},{1},{2}\n".format(kor, math, grade))
    
fp.close()


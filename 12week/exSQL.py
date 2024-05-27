import sqlite3
import sys

'''
CREATE TABLE data (
   id INTEGER AUTO_INCREMENT,
   time datetime DEFAULT current_timestamp,
   kor INTEGER,
   math INTEGER,
   grade char(1),
   PRIMARY KEY(id) 
)
'''

DATABASE_FILE = "grade.db"

sqlite3 = sqlite3.connect(DATABASE_FILE)

try:
    cursor = sqlite3.cursor()
    cursor.execute("DROP TABLE IF EXISTS data")
    cursor.execute("CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, time datetime DEFAULT current_timestamp, kor INTEGER, math INTEGER, grade char(1))")
    sqlite3.commit()
except:
    sqlite3.rollback()
    sqlite3.close()
    sys.exit("테이블 생성 실패")
    
    
fp = open("grade.csv", "r", encoding="utf-8")
if not fp:
    sqlite3.close()
    sys.exit("파일 읽기 실패")
    
fp.readline()
for line in fp:
    line = line.strip()
    kor, math, grade = line.split(",")
    try:
        cursor.execute("INSERT INTO data (kor, math, grade) VALUES (?,?,?)", (kor, math, grade))
    except:
        sqlite3.rollback()
        sqlite3.close()
        sys.exit("데이터 삽입 실패")
        

sqlite3.commit()
fp.close()

try:
    cursor.execute("SELECT * FROM data WHERE grade = 'A' and kor > 95 and math > 95")
    rows = cursor.fetchall()
    print("A인 데이터 개수: {0}".format(len(rows)))
    print(rows)
except:
    sqlite3.rollback()
    sqlite3.close()
    sys.exit("데이터 조회 실패")
    
sqlite3.close()
print("Done")



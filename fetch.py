import sqlite3

con = sqlite3.connect('StudDetails01.db')

cur = con.cursor()

data = cur.execute('''select * from StudDetails01''')

for row in data:
    rollNo = row[0]
    studName = row[1]
    phyMarks = row[2]
    cheMarks = row[3]
    mathMarks = row[4]
    print(str(rollNo) + "   " + studName + "   " + str(phyMarks) + "   " + str(cheMarks)+"   " + str(mathMarks))

con.close()
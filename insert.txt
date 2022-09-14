import sqlite3

con = sqlite3.connect('StudDetails01.db')

cur = con.cursor()

cur.execute('''INSERT INTO StudDetails01 (RollNo, StudName, PhyMarks,CheMarks, MathMarks)  VALUES (101, 'MAN', 70, 80, 56)''')

cur.execute('''INSERT INTO StudDetails01 (RollNo, StudName, PhyMarks,CheMarks, MathMarks)  VALUES (102, 'WOMEN', 77, 88, 77)''')

con.commit()
con.close()
import sqlite3, random


class DB:
    # 생성자
    # DB와 연결
    def __init__(self, fileName):
        self.conn = sqlite3.connect(fileName)
        self.cur = self.conn.cursor()

    # 데이터베이스 생성
    def createDateBase(self, query):
        self.query = query
        self.excuteQuery(self.query)

    # 입력된 쿼리문장 실행
    def excuteQuery(self, query):
        self.cur.execute(query)

    def addData(self, sNo, sName, hp):
        query = 'INSERT INTO student VALUES ({0}, "{1}", "{2}");'.format(sNo, sName, hp)
        self.excuteQuery(query)
        self.conn.commit()

    def deleteData(self, sNo):
        query = 'DELETE FROM student WHERE sno = "{0}"'.format(sNo)
        self.excuteQuery(query)
        self.conn.commit()

    def search(self):
        query = 'SELECT student.sname FROM student, enrol WHERE student.sno = enrol.sno AND enrol.grade >= 60'
        self.excuteQuery(query)
        for rec in self.cur.fetchall():
            print(rec)

    # 데이터베이스에 기록된 정보를 보여준다
    def showDataBase(self):
        self.cur.execute('SELECT * FROM student')
        self.conn.commit()
        for rec in self.cur.fetchall():
            print(rec)


fileName = 'student.db'
query = '''CREATE TABLE IF NOT EXISTS student (
sno INTEGER NOT NULL,
sname VARCHAR(4),
hp VARCHAR(13),
PRIMARY KEY (sno),
UNIQUE (sno))'''

db = DB(fileName)
db.createDateBase(query)
# db.addData(20113250, 'A', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113251, 'B', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113252, 'C', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113253, 'D', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113254, 'E', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113255, 'F', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113256, 'G', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113257, 'H', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113258, 'I', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113259, 'J', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.addData(20113260, 'K', '010-{0}-{1}'.format(random.randint(0000, 9999), random.randint(0000, 9999)))
# db.search()
# db.showDataBase()

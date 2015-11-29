import sqlite3


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

    def addData(self, sNo, cNo, grade):
        query = 'INSERT INTO enrol VALUES ({0}, "{1}", {2});'.format(sNo, cNo, grade)
        self.excuteQuery(query)
        self.conn.commit()

    def deleteData(self, sNo, cNo):
        query = 'DELETE FROM enrol WHERE sno = "{0}" AND cno = "{1}"'.format(sNo, cNo)
        self.excuteQuery(query)
        self.conn.commit()

    def search(self):
        query = 'SELECT * FROM enrol WHERE sno = 20113259'
        self.excuteQuery(query)
        for rec in self.cur.fetchall():
            print(rec)

    # 데이터베이스에 기록된 정보를 보여준다
    def showDataBase(self):
        self.cur.execute('SELECT * FROM enrol')
        self.conn.commit()
        for rec in self.cur.fetchall():
            print(rec)


fileName = 'enrol.db'
query = '''CREATE TABLE IF NOT EXISTS enrol (
sno INTEGER NOT NULL,
cno VARCHAR(4) NOT NULL,
grade INTEGER,
PRIMARY KEY(sno, cno),
FOREIGN KEY(sno) REFERENCES student
	ON DELETE CASCADE
	ON UPDATE CASCADE,
FOREIGN KEY(cno) REFERENCES course
	ON DELETE CASCADE
	ON UPDATE CASCADE,
CHECK(grade >= 0 AND grade <= 100));'''

db = DB(fileName)
db.createDateBase(query)
# db.addData(20113259, 'C413', 60)
# db.addData(20113259, 'C512', 50)
db.showDataBase()

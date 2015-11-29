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

    def addData(self, cNo, pro):
        query = 'INSERT INTO course VALUES ("{0}", "{1}");'.format(cNo, pro)
        self.excuteQuery(query)
        self.conn.commit()

    def deleteData(self, cNo):
        query = 'DELETE FROM course WHERE cno = "{0}"'.format(cNo)
        self.excuteQuery(query)
        self.conn.commit()

    def search(self):
        query = 'SELECT * FROM course WHERE sno = 20113259'
        self.excuteQuery(query)
        for rec in self.cur.fetchall():
            print(rec)

    # 데이터베이스에 기록된 정보를 보여준다
    def showDataBase(self):
        self.cur.execute('SELECT * FROM course')
        self.conn.commit()
        for rec in self.cur.fetchall():
            print(rec)


fileName = 'course.db'
query = '''CREATE TABLE IF NOT EXISTS course (
cno VARCHAR(4) NOT NULL,
pro VARCHAR(4),
PRIMARY KEY (cno),
UNIQUE (cno));'''

db = DB(fileName)
db.createDateBase(query)
# db.addData('C413', '김보운')
db.showDataBase()

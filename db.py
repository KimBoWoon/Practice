__author__ = 'user'

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

    # 파일에 입력된 정보를 가져옴
    def readFile(self):
        with open('DATA', 'r') as f:
            self.s = f.read()
            self.s = self.s.split()

    # 파일에서 가져온 정보를 데이터 베이스에 추가
    def addDataBase(self):
        i = 0
        while True:
            dataFormat = '{0}-{1}-{2} {3}:{4}'.format(self.s[i][0:4], self.s[i][4:6], self.s[i][6:8], self.s[i][8:10],
                                                      self.s[i][10:12])
            self.query = 'INSERT INTO data VALUES (\'{0}\', {1}, {2}, {3})'.format(
                dataFormat, self.s[i + 1], self.s[i + 2],
                self.s[i + 3], )
            i += 4
            # 정보를 4개씩 읽어들어야함
            # 길이가 파일의 길이를 넘어서면 반복 종료
            if (i + 4 >= len(self.s)):
                break
            self.excuteQuery(self.query)
        self.conn.commit()

    # 데이터베이스에 기록된 정보를 보여준다
    def showDataBase(self):
        self.cur.execute('select * from data')
        self.conn.commit()
        for rec in self.cur.fetchall():
            print(rec)


fileName = 'data.db'
query = '''CREATE TABLE IF NOT EXISTS data (
data DATE,
temp VARCHAR(4),
humi VARCHAR(4),
asto VARCHAR(4))'''

db = DB(fileName)
db.createDateBase(query)
db.readFile()
db.addDataBase()
db.showDataBase()

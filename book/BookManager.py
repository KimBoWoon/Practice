__author__ = 'user'

from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END, ttk, W, E
import sqlite3


class BookManager(Frame):
    # 생성자
    # DB와 연결
    # 라벨과 엔트리 생성
    # UI 초기 설정
    # 윈도우 중앙 위치
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.conn = sqlite3.connect('bookInfo.db')
        self.cur = self.conn.cursor()
        self.parent = parent
        self.nameLabel = StringVar()
        self.authorLabel = StringVar()
        self.priceLabel = StringVar()
        self.infoLabel = StringVar()
        self.nameEntry = ttk.Entry(self)
        self.authorEntry = ttk.Entry(self)
        self.priceEntry = ttk.Entry(self)
        self.initUI()
        self.centerWindow()

    # 윈도우 생성과 위젯에 배치를 담당
    def initUI(self):
        self.parent.title("Book DataBase")
        self.pack(fill=BOTH, expand=1)

        self.lb = Listbox(self, height=15, width=93)
        self.lb.place(x=20, y=100)

        # 라벨을 생성해서 화면에 뿌려줌
        self.createLabel(65, 25, self.nameLabel, '책 이름 : ')
        self.createLabel(65, 45, self.authorLabel, '저     자: ')
        self.createLabel(65, 65, self.priceLabel, '가     격: ')
        # 엔트리를 생성해서 화면에 뿌려줌
        self.createEntry(2, 1, self.nameEntry)
        self.createEntry(3, 1, self.authorEntry)
        self.createEntry(4, 1, self.priceEntry)

        # 버튼 생성과 이벤트 연결
        add = ttk.Button(self, text="ADD", command=lambda: self.addBook())
        add.grid(row=1, column=0, padx=20)
        delete = ttk.Button(self, text="DEL", command=lambda: self.delBook())
        delete.grid(row=1, column=1, padx=20)
        search = ttk.Button(self, text="SEARCH", command=lambda: self.search())
        search.grid(row=1, column=2, padx=20)
        show = ttk.Button(self, text="SHOW", command=lambda: self.showBookInfo())
        show.grid(row=1, column=3, padx=20)

        # 책 정보를 출력
        self.showBookInfo()

    # 전달받은 인자를 통해 적재적소에 라벨 생성
    def createLabel(self, x, y, o, s):
        o.set(s)
        self.label = Label(self, text=0, textvariable=o)
        self.label.place(x=x, y=y)

    # 전달받은 인자를 통해 적재적소에 엔트리 위치
    def createEntry(self, row, col, o):
        o.grid(row=row, column=col, columnspan=4, sticky=W + E)

    # 윈도우 중앙 위치
    def centerWindow(self):
        w = 700
        h = 400

        # screen 크기를 구함
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # 쿼리 실행 담당
    def execteQuery(self, query):
        self.query = query
        self.cur.execute(query)
        self.conn.commit()

    # 책 정보를 검색한다
    def search(self):
        # 리스트를 모두 지운다
        self.lb.delete(0, END)

        # 이름에 값이 존재할 경우
        if (self.nameEntry.get() != ''):
            # 어느정도만 입력해도 검색할 수 있도록 쿼리문 작성
            self.query = 'select count (*) from book where name like \'%{0}%\''.format(self.nameEntry.get())
            self.execteQuery(self.query)
            # 책 정보가 존재하지 않을 경우
            if ('{0}', format(self.cur.fetchone()) == 0):
                self.createLabel(20, 350, self.infoLabel, '해당하는 정보가 존재하지 않습니다')

            # 책 정보가 존재할 때 패턴 정보를 가진 책을 모두 가져옴
            self.query = 'select * from book where name like \'%{0}%\''.format(self.nameEntry.get())
            self.execteQuery(self.query)
        # 저자에 값이 존재할 경우
        elif (self.authorEntry.get() != ''):
            # 어느정도만 입력해도 검색할 수 있도록 쿼리문 작성
            self.query = 'select count (*) from book where name like \'%{0}%\''.format(self.authorEntry.get())
            self.execteQuery(self.query)
            # 책 정보가 존재하지 않을 경우
            if ('{0}', format(self.cur.fetchone()) == 0):
                self.createLabel(20, 350, self.infoLabel, '해당하는 정보가 존재하지 않습니다')

            # 책 정보가 존재할 때 패턴 정보를 가진 책을 모두 가져옴
            self.query = 'select * from book where author like \'%{0}%\''.format(self.authorEntry.get())
            self.execteQuery(self.query)
        # 값이 입력되지 않았을 때
        else:
            self.createLabel(20, 350, self.infoLabel, '정보를 정확히 입력해주세요')
            return

        # 검색된 책 정보를 출력
        for book in self.cur.fetchall():
            print(book)
            s = '책 이름 : {0[0]:30}저    자 : {0[1]:30}가    격 : {0[2]:30}'.format(book)
            self.lb.insert(END, s)

    # 모든 책 정보를 출력
    def showBookInfo(self):
        temp = ''

        self.lb.delete(0, END)
        # 모든 정보를 가져오는 쿼리문
        self.query = 'select * from book'
        self.execteQuery(self.query)
        # 책을 제거 했을 때 동일한 정보를 가진 책 정보가 본의 아니게 만들어 져서
        # 임시값을 이용해 같은 정보가 있는지 검사하여 없을 경우 출력
        for book in self.cur.fetchall():
            rec = '책 이름 : {0[0]:30}저    자 : {0[1]:30}가    격 : {0[2]:30}'.format(book)
            if (temp == rec):
                continue
            self.lb.insert(END, rec)
            temp = rec

    # 책 정보 추가
    def addBook(self):
        # 책 정보를 입력할 때 책 이름, 저자, 가격 정보가 모두 필요함
        if (self.nameEntry.get() == '' or self.authorEntry.get() == '' or self.priceEntry.get() == ''):
            self.createLabel(20, 350, self.infoLabel, '정보를 정확히 입력해주세요')
            return

        # 책 정보를 추가하는 쿼리문
        self.query = 'INSERT INTO book VALUES (\'{0}\', \'{1}\', \'{2}\')'.format(self.nameEntry.get(),
                                                                                  self.authorEntry.get(),
                                                                                  self.priceEntry.get())
        self.cur.execute(self.query)
        self.createLabel(20, 350, self.infoLabel, '추가완료')
        self.showBookInfo()
        self.clearEntry()

    # 책 정보 제거
    def delBook(self):
        # 책을 제거할 때 책 이름과 저자정보 모두가 있어야 제거가 가능하도록 구현
        if (self.nameEntry.get() == '' or self.authorEntry.get() == ''):
            self.createLabel(20, 350, self.infoLabel, '정보를 정확히 입력해주세요')
            return

        # 책 정보를 제거하는 쿼리문
        self.query = 'DELETE FROM book WHERE name = \'{0}\' and author = \'{1}\''.format(self.nameEntry.get(),
                                                                                         self.authorEntry.get())
        self.cur.execute(self.query)
        self.showBookInfo()
        self.createLabel(20, 350, self.infoLabel, '제거완료')
        self.clearEntry()

    # 책 정보가 입력되고 제거되었을 때 다시 입력할 수 있도록 엔트리를 비워준다
    def clearEntry(self):
        self.nameEntry.delete(0)
        self.authorEntry.delete(0)
        self.priceEntry.delete(0)


def main():
    query = '''CREATE TABLE IF NOT EXISTS book (
    name VARCHAR(30),
    author VARCHAR(10),
    price VARCHAR(10))'''
    root = Tk()
    manager = BookManager(root)
    manager.execteQuery(query)
    root.mainloop()


if __name__ == '__main__':
    main()

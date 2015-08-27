__author__ = 'user'

from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END, ttk, W, E


# {'name': '뇌를 자극하는 알고리즘', 'author': '박상현', 'price': '25000'}
# {'name': '뇌를 자극하는 윈도우즈 시스템 프로그래밍', 'author': '윤성우', 'price': '29000'}
# {'name': '열혈강의 C프로그래밍', 'author': '윤성우', 'price': '20000'}
# {'name': '열혈강의 자료구조', 'author': '윤성우', 'price': '23000'}
# {'name': '열혈강의 C++프로그래밍', 'author': '윤성우', 'price': '25000'}
# {'name': '열혈강의 TCP/IP 프로그래밍', 'author': '윤성우', 'price': '18000'}
# {'name': '초보자를 위한 C언어 300제', 'author': '김은철', 'price': '23000'}
# {'name': '초보자를 위한 JAVA 200제', 'author': '조효은', 'price': '25000'}
# {'name': '뇌를 자극하는 C++ STL', 'author': '공동환', 'price': '22000'}
# {'name': '안드로이드 프로그래밍 정복', 'author': '김상형', 'price': '31500'}

# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Listbox")
#         self.pack(fill=BOTH, expand=1)
#
#         acts = ['Scarlett Johansson', 'Rachel Weiss',
#             'Natalie Portman', 'Jessica Alba']
#
#         lb = Listbox(self)
#         for i in acts:
#             lb.insert(END, i)
#
#         lb.bind("<<ListboxSelect>>", self.onSelect)
#
#         lb.place(x=20, y=20)
#
#         self.var = StringVar()
#         self.label = Label(self, text=0, textvariable=self.var)
#         self.label.place(x=20, y=210)
#
#     def onSelect(self, val):
#
#         sender = val.widget
#         idx = sender.curselection()
#         value = sender.get(idx)
#
#         self.var.set(value)
#
#
# def main():
#
#     root = Tk()
#     ex = Example(root)
#     root.geometry("300x250+300+300")
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()

class BookManager(Frame):
    book = []

    def __init__(self, parent):
        self.fileReadBook()
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.parent.title("Listbox")
        self.pack(fill=BOTH, expand=1)

        self.lb = Listbox(self, height=15, width=93)
        for i in self.book:
            s = '책 이름 : {name}, 저자 : {author}, 가격 : {price}원'.format_map(i)
            self.lb.insert(END, s)

        self.lb.bind("<<ListboxSelect>>", self.onSelect)

        self.lb.place(x=20, y=400)

        self.name = StringVar()
        self.name.set('책 이름 : ')
        self.label = Label(self, text=0, textvariable=self.name)
        self.label.place(x=70, y=25)
        self.entry1 = ttk.Entry(self)
        self.entry1.grid(row=2, column=1, columnspan=4, sticky=W + E)

        self.auhtor = StringVar()
        self.auhtor.set('저     자: ')
        self.label = Label(self, text=0, textvariable=self.auhtor)
        self.label.place(x=70, y=45)
        self.entry2 = ttk.Entry(self)
        self.entry2.grid(row=3, column=1, columnspan=4, sticky=W + E)

        self.price = StringVar()
        self.price.set('가     격: ')
        self.label = Label(self, text=0, textvariable=self.price)
        self.label.place(x=70, y=65)
        self.entry3 = ttk.Entry(self)
        self.entry3.grid(row=4, column=1, columnspan=4, sticky=W + E)

        add = ttk.Button(self, text="ADD", command=lambda: self.addBook())
        add.grid(row=1, column=0, padx=20)
        delete = ttk.Button(self, text="DEL", command=lambda: self.delBook(''))
        delete.grid(row=1, column=1, padx=20)
        search = ttk.Button(self, text="SEARCH", command=lambda: self.search(''))
        search.grid(row=1, column=2, padx=20)
        show = ttk.Button(self, text="SHOW", command=lambda: self.showBookInfo())
        show.grid(row=1, column=3, padx=20)

    def centerWindow(self):
        w = 700
        h = 700

        # screen 크기를 구함
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onSelect(self, val):

        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)

    def fileReadBook(self):
        with open('bookInfo', 'r') as f:
            while True:
                bookDic = {}
                # 파일을 읽어옴
                name = f.readline()
                author = f.readline()
                price = f.readline()

                # 파일의 마지막을 의미
                if (name == '' and author == '' and price == ''):
                    break

                # 개행문자를 제외한 나머지 문자열을 저장
                bookDic['name'] = name[:-1]
                bookDic['author'] = author[:-1]
                bookDic['price'] = price[:-1]

                # 읽어 들여온 책정보를 리스트에 저장
                self.book.append(bookDic)

    def nameSearch(self, name):
        i = 0
        for x in self.book:
            if (x['name'] == name):
                print(x)
            i += 1

    def authorSearch(self, author):
        i = 0
        for x in self.book:
            if (x['author'] == author):
                print(x)
            i += 1

    def search(self, author):
        i = 0
        for x in self.book:
            if (x['name'] == author):
                return i
            i += 1

    def showBookInfo(self):
        for x in self.book:
            print(x['name'] + ', ' + x['author'] + ', ' + x['price'])
            # for x in self.book:
            #     print(x)

    def addBook(self):
        dic = {}
        name = self.entry1.get()
        author = self.entry2.get()
        price = self.entry3.get()

        dic['name'] = name
        dic['author'] = author
        dic['price'] = price

        if (name == '' or author == '' or price == ''):
            return

        # self.book.append({'name': name, 'author': author, 'price': price})
        self.book.append(dic)
        s = '책 이름 : {name}, 저자 : {author}, 가격 : {price}원'.format_map(dic)
        self.lb.insert(END, s)

        self.var = StringVar()
        self.var.set('추가완료')
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.place(x=20, y=310)

        self.entry1.config(textvariable=' ')
        self.entry2.config(textvariable=' ')
        self.entry3.config(textvariable=' ')

    def delBook(self, name):
        i = self.search(name)
        del self.book[i]


def main():
    root = Tk()
    ex = BookManager(root)
    # root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
# if __name__ == '__main__':
#     manager = BookManager()
#     manager.showBookInfo()
#     manager.authorSearch('윤성우')

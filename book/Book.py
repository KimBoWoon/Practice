__author__ = 'user'

# book = [
#     {'name': '뇌를 자극하는 알고리즘', 'author': '박상현', 'price': '25000'},
#     {'name': '뇌를 자극하는 윈도우즈 시스템 프로그래밍', 'author': '윤성우', 'price': '29000'},
#     {'name': '열혈강의 C프로그래밍', 'author': '윤성우', 'price': '20000'},
#     {'name': '열혈강의 자료구조', 'author': '윤성우', 'price': '23000'},
#     {'name': '열혈강의 C++프로그래밍', 'author': '윤성우', 'price': '25000'},
#     {'name': '열혈강의 TCP/IP 프로그래밍', 'author': '윤성우', 'price': '18000'},
#     {'name': '초보자를 위한 C언어 300제', 'author': '김은철', 'price': '23000'},
#     {'name': '초보자를 위한 JAVA 200제', 'author': '조효은', 'price': '25000'},
#     {'name': '뇌를 자극하는 C++ STL', 'author': '공동환', 'price': '22000'},
#     {'name': '안드로이드 프로그래밍 정복', 'author': '김상형', 'price': '31500'}
# ]

class Book:
    name = ''
    author = ''
    price = ''

    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def showBookInfo(self):
        print('name : ' + self.name + ', author : ' + self.author + ', price : ' + self.price)

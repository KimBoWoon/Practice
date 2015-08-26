__author__ = 'user'

from socket import *

PORT = 2000
IP = '127.0.0.1'

svrSock = socket(AF_INET, SOCK_STREAM)
svrSock.connect((IP, PORT))
# 사용자 이름 입력
s = input('name : ')
# 이름을 서버에 전송
# 바이트타입으로 전송해야 되기 때문에 인코딩을 해준다
# 인코딩함수에 인코딩 디폴트 매개변수가 UTF-8인데?
# 그럼 전송할때 바이트타입이 아닌 스트링 타입이 전송되는게 아닌가?
# 에러가 안뜨는게 이상한거 같다(건전한 의심인거 같은데??)
svrSock.send(s.encode())
while True:
    # 사용자에게 문자열을 입력받는다
    data = input('message >> ')
    # 사용자가 입력한 문자열이 EXIT일 경우 채팅종료를 의미
    # 서버에서 사용자 카운트를 하기위해 EXIT란 문자열 전송
    # 소켓 종료(이건 소켓 정상 종료 함수가 맞겠지?)
    if ('EXIT' == data):
        svrSock.send(data.encode())
        svrSock.close()
        break
    svrSock.send(data.encode())
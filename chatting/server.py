__author__ = 'user'

from socketserver import ThreadingTCPServer, StreamRequestHandler

PORT = 2000
IP = '127.0.0.1'


class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        # 채팅 이용자 체크
        cnt = 0
        conn = self.request
        # 사용자 이름
        name = conn.recv(1024)
        # print('connection from', self.client_address)
        print(name.decode('utf-8') + '님이 입장하셨습니다!')
        # 사용자가 입장했으므로 카운트 증가
        cnt += 1
        while True:
            buf = conn.recv(1024)
            if not buf:
                pass
            # 퇴장
            elif buf.decode('utf-8') == 'EXIT':
                print(name.decode('utf-8') + '님이 퇴장하셨습니다!')
                cnt -= 1
                # 카운트가 0이면 채팅 이용자가 없으므로 서버 종료
                # 서버(스레드) 종료 함수를 잘모르겠다
                # 왠지 shutdown() 함수는 강제종료인것같다
                # 정상 종료 함수 없나?
                if (0 == cnt):
                    server.shutdown()
                    return
            else:
                # 사용자들이 입력한 문자열을 UTF-8로 인코딩하여 출력
                print(name.decode('utf-8') + ' : ' + buf.decode('utf-8'))


server = ThreadingTCPServer((IP, PORT), MyRequestHandler)
print('listening on port', PORT)
server.serve_forever()
# 이 함수가 스레드 종료 함수 아닌가?
# server.server_close()

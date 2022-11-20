import socket, threading
from tcp_by_size import *

IP_PORT = ('0.0.0.0', 80)
clients = []
LINE = r'\r\n'

def build_answer(fields):
    if '/' in fields:
        html_file = open('login.html')
        data = '\n'.join(x for x in html_file.readlines())
        length = str(len(str(html_file)))
        answer = 'HTTP/1.1 200 OK' + LINE 
        answer += 'Content-Length: ' + length + LINE
        answer  += 'Content-Type: text/html; charset=utf-8' + LINE 
        answer += LINE
        answer += data
        html_file.close()   
        return answer

def handle_client(c_sock, addres, id):

    while True:
        data = c_sock.recv(1024).decode()
        print(data)
        fields = data.split('\r\n')[0].split()
        response = build_answer(fields)
        if response is not None:
            c_sock.send(response.encode())
    pass

def main():
    s = socket.socket()

    s.bind(IP_PORT)
    s.listen(3)
    i = 0
    while i < 4:
        c, add = s.accept()
        print("connected")
        t = threading.Thread(target=handle_client, args=(c,add, i))
        t.start()
        clients.append(t)
        i += 1

    s.close()
    pass


if __name__ == '__main__':
    main()
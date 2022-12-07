import socket, threading
from tcp_by_size import *

IP_PORT = ('0.0.0.0', 80)
clients = []
LINE = r'\r\n'
current_page = ''
user = ['guest']


def website_request(file_name): 
    if file_name == '/':
        file_name = '/home.html'
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!' + file_name)
    html_file = open('pages' + file_name)
    data = '\n'.join(x for x in html_file.readlines())
    length = str(len(str(html_file)))
    answer = 'HTTP/1.1 200 OK' + LINE 
    answer += 'Content-Length: ' + length + LINE
    answer  += 'Content-Type: text/html; charset=utf-8' + LINE 
    answer += 'Set-Cookie: name=3' + LINE
    answer += LINE
    answer += data
    html_file.close()
    return answer


def validate_user(params):
    global user
    if params > 1:
        user[0] = 'ap'
        # appraiser = Appraiser
    else:
        user[0] = 'cli'
    

def build_answer(fields):
    ans = ''
    pic = ''
    if '?' in fields:
        pass
    if len(fields) > 1 and '/' in fields[1] and '?' not in fields[1]:
        ans = website_request(fields[1])
        # pic = send_assests(fields[1])
    return ans


def handle_client(c_sock, addres, id):

    while True:
        data = c_sock.recv(1024).decode()
        print(data)
        fields = data.split('\r\n')[0].split()
        response = build_answer(fields) 
        print(response)
        if response is not None:
            c_sock.send(response.encode())

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
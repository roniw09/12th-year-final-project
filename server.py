import socket, threading, os
from tcp_by_size import *

IP_PORT = ('0.0.0.0', 80)
clients = []
LINE = r'\r\n'
current_page = ''
user = ['guest']


def file_contetn_type(file_name):
    path = ''
    content = ''
    f_type = file_name.split('.')[-1]
    if os.path.exists(f'page{file_name}'):
        path = f'page{file_name}'
    elif os.path.exists(f'assests{file_name}'):
        path = f'assests{file_name}'
    if path == '':
        return 'Err'
    with open(path) as file:
        content += '\n'.join(x for x in file.readlines())
    return f_type, content


def website_request(file_name): 
    if file_name == '/':
        file_name = '/home.html'
    f_type, file = file_contetn_type(file_name)
    if not file:
        return ''
    length = str(len(str(file)))
    answer = 'HTTP/1.1 200 OK' + LINE 
    answer += 'Content-Length: ' + length + LINE
    answer  += f'Content-Type: {type}; charset=utf-8' + LINE 
    answer += 'Set-Cookie: name=3' + LINE
    answer += LINE
    answer += data    
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
    i = 0
    data = c_sock.recv(1024).decode()
    print(data)
    fields = data.split('\r\n')[0].split()
    response = build_answer(fields) 
    if response is not None:
        c_sock.send(response.encode())
    c_sock.close()

def main():
    s = socket.socket()

    s.bind(IP_PORT)
    s.listen(20)
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
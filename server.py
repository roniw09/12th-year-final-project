import socket, threading, os
from ORM import *
from createPages import CreatePages

IP_PORT = ('0.0.0.0', 80)
clients = []
LINE = r'\r\n'
current_page = ''
user = ['guest']


def file_content_type(file_name):
    path = ''
    content = ''
    if file_name == '/':
        file_name = '/home.html' 
    f_type = file_name.split('.')[-1]
    file_name = '\\' + file_name[1:]
    if os.path.exists(f'pages{file_name}'):
        path = f'pages{file_name}'
    elif os.path.exists(f'assests{file_name}'):
        path = f'assests{file_name}'
    if path == '':
        return 'Err'
    c_file = open(path, encoding='utf-8')
    content += '\n'.join(x for x in c_file.readlines())
    c_file.close()
    return [f_type, content] 


def website_request(file_name): 
    file_content = file_content_type(file_name)
    if 'Err' in file_content:
        return ''
    length = str(len(str(file_content[1])))
    answer = 'HTTP/1.1 200 OK' + LINE 
    answer += 'Content-Length: ' + length + LINE
    answer  += f'Content-Type: {file_content[0]}; charset=utf-8' + LINE 
    answer += LINE
    answer += file_content[1]  
    return answer


def validate_user(params):
    global user
    if type(params) == type([]):
        user[0] = 'ap'
        data = ORM.get_employee_data(params[0], params[1])
    else:
        user[0] = 'cli'
        data = ORM.get_client_data(params)
    return data



def extract_answer(data):
    web = data.split('?')[0]
    fields = data.split('?')[1].split('=')
    username = fields[1].split('&')[0]
    password = fields[2] 
    return [username, password], web  

def build_answer(fields):
    ans = ''
    pic = ''
    if fields[0] == 'GET':
        if '?' in fields[1]:
            if 'uname' in fields[1] or 'number' in fields[1]:
                details, web = extract_answer(fields[1])
                if '05' in details[0]:
                    details = details[0] + '-' + details[1]
                res = validate_user(details)
                if res == 'ERR1':
                    web = '/Error.html'
                elif user[0] == 'ap':
                    CreatePages.validated_appraiser_page(details[0], details[1])
                elif user[0] == 'cli':
                    CreatePages.validated_client_page(res)
                fields = ['', web]
        if '/' in fields[1] and '?' not in fields[1]:
            ans = website_request(fields[1])
    return ans


def handle_client(c_sock, addres, id):
    i = 0
    data = c_sock.recv(1024).decode()
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
    while i < 20:
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

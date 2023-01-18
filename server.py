import socket, threading, os
from ORM import *
from createPages import CreateClientPages

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
    print(file_name)
    if os.path.exists(f'pages{file_name}'):
        path = f'pages{file_name}'
    elif os.path.exists(f'assests{file_name}'):
        path = f'assests{file_name}'
    if path == '':
        return 'Err'
    c_file = open(path)
    content += '\n'.join(x for x in c_file.readlines())
    c_file.close()
    return [f_type, content] 


def website_request(file_name): 
    print(file_name)
    file_content = file_content_type(file_name)
    print(file_content  )
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
    if len(params)> 1:
        user[0] = 'ap'
        data = ORM.get_employee_data(params[0], params[1])
        print(data)
    else:
        user[0] = 'cli'
    

def build_answer(fields):
    ans = ''
    pic = ''
    if fields[0] == 'GET':
        if '?' in fields[1]:
            print("entered form")
            web = fields[1].split('?')[0]
            fields = fields[1].split('?')[1].split('=')
            username = fields[1].split('&')[0]
            password = fields[2]
            print("!!!!!!!!!!!!!!!")
            res = validate_user([username,password])
            if res == 'UserErr':
                return res
            if user[0] == 'ap':
                CreateClientPages.validated_appraiser_page(username, password)
            print(web)
            fields = ['', web]
        if '/' in fields[1] and '?' not in fields[1]:
            ans = website_request(fields[1])
            # pic = send_assests(fields[1])
    return ans


def handle_client(c_sock, addres, id):
    i = 0
    data = c_sock.recv(1024).decode()
    print(data)
    fields = data.split('\r\n')[0].split()
    print(fields)
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
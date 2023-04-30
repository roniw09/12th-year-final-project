import socket, threading, os
import datetime
from ORM import *
from usersClasses import * 
from createPages import CreatePages
from chat import *

IP_PORT = ('0.0.0.0', 80)
clients = []
LINE = r'\r\n'
current_page = ''


def file_content_type(file_name):
    path = ''
    content = ''
    if file_name == '/':
        file_name = '/home.html' 
    if "favicon" in file_name:
        return ""
    f_type = file_name.split('.')[-1]
    file_name = '\\' + file_name[1:]
    if os.path.exists(f'pages{file_name}'):
        path = f'pages{file_name}'
    elif os.path.exists(f'assests{file_name}'):
        path = f'assests{file_name}'
    if path == '':
        return 'Err'
    c_file = open(path, 'r', encoding="utf-8")
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
    user = []
    if type(params) == type([]):
        user.append('ap')
        data = ORM.get_employee_data(params[0], params[1])
        if data == 'ERR1':
            return 'ERR1'
        user.append(Appraiser(data[0], data[1], data[-1]))
        print(user[1])
    else:
        user.append('cli')
        data = ORM.get_client_data(params)
        print(data)
        if data == 'ERR1':
            return 'ERR1'
        add = Address(data[7], data[8], data[9])
        if data[5] != None and data[6] != None:
            exeTime = datetime(data[5].year, data[5].month, data[5].day, data[6].hour, data[6].minute)
        else:
            exeTime = None
        user.append(Client(data[0], data[1], data[2], data[3], data[4], add, exeTime, data[10]))
    return user


def extract_date(data):
    extract = data.split('?')
    web = extract[0]
    splitDateTime = extract[-1].split('=')
    ymd = splitDateTime[1].split('&')[0]
    hm = splitDateTime[-1].split('%3A')
    hm = f'{hm[0].zfill(2)}:{hm[-1].zfill(2)}'
    print(ymd, hm)
    return web, ymd, hm

def get_user_from_cookie(cookie):
    print(cookie)
    user = ''
    if cookie == None:
        return 'Err'
    c_type, c_id = cookie[1].split('=')
    if c_type == 'appraiser':
        data = ORM.get_app_by_id(c_id)
        user = Appraiser(data[0], data[1], data[-1])
    else:
        data = ORM.get_cli_by_id(c_id)
        add = Address(data[7], data[8], data[9])
        if data[5] != None and data[6] != None:
            exeTime = datetime.datetime(data[5].year, data[5].month, data[5].day, data[6].hour, data[6].minute)
        else:
            exeTime = None
        user = Client(data[0], data[1], data[2], data[3], data[4], add, exeTime, data[10])
    return user

def extract_login_answer(data):
    web = data.split('?')[0]
    fields = data.split('?')[1].split('=')
    username = fields[1].split('&')[0]
    password = fields[2] 
    return [username, password], web
 
def extractSekerData(formAnswers):
    web, dataOnly = formAnswers.split('?')[0], formAnswers.split('?')[1]
    dataOnly = dataOnly.split('&')
    print(web, dataOnly)
    sekerId = dataOnly[0].split('=')[1]
    itemsNprices = [x.split('=')[1] for x in dataOnly[1:]]
    return web, sekerId, itemsNprices

def build_answer(fields, cookie):
    print(cookie)
    ans = ''
    pic = ''
    if fields[0] == 'GET':
        if '?' in fields[1]:
            if 'uname' in fields[1] or 'number' in fields[1]:
                details, web = extract_login_answer(fields[1])
                print(web)
                if '05' in details[0]:
                    details = details[0] + '-' + details[1]
                user = validate_user(details)
                if user == 'ERR1':
                    web = '/Error.html'
                elif user[0] == 'ap':
                    CreatePages.validated_appraiser_page(user[1])
                elif user[0] == 'cli':
                    CreatePages.validated_client_page(user[1])
                fields = ['', web]
            elif 'selected' in fields[1]:
                web, dateSelected, timeSelected = extract_date(fields[1])
                ORM.updateCliSekerDate(dateSelected, timeSelected, cookie[-1].split('=')[-1])
                fields = ['', web]
            elif 'Seker' in fields[1]:
                web, sekerId, sekerData = extractSekerData(fields[1])
                ORM.updateSeker(sekerId, sekerData)
                fields = ['', web]
            elif 'msg' in fields[1]:
                reciever, msg = fields[1].split('?')[1].split('&')
                reciever = reciever.split('=')
                msg= msg.split('=')[1]
                res = update_send_msg(reciever, msg, cookie)
                web = fields[1].split('?')[0]
                print(web)
                fields = ['', web]
        if '/' in fields[1] and '?' not in fields[1]:
            if 'chat' in fields[1]:
                user = get_user_from_cookie(cookie)
                print(user, type(user))
                web = CreatePages.go_chat(user)
            ans = website_request(fields[1])
    return ans


def handle_client(c_sock, addres, id):
    i = 0
    data = c_sock.recv(1024).decode()
    print("CURRENT REQUEST:\n",data)
    cookie = data.split('\r\n')[-3].split()
    fields = data.split('\r\n')[0].split()
    response = build_answer(fields, cookie) 
    if response is not None:
        c_sock.send(response.encode())
    c_sock.close()

def main():
    s = socket.socket()

    s.bind(IP_PORT)
    s.listen(100)
    i = 0
    while i < 100:
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

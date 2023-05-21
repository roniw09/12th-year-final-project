import socket, threading, os, urllib.parse
import datetime
from ORM import *
from usersClasses import * 
from createPages import CreatePages
from chat import *
from seker import *

IP_PORT = ('0.0.0.0', 80)
clients = []
LINE = r'\r\n'
current_page = ''


def file_content_type(file_name):
    """
        determine the content type of a file based on its extension and retrieve its content.
    """
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


def website_request(file_name, cookie):
    """
        write the http website request, including retrieving the file content and constructing the HTTP response.
    """
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
    """
        validate user credentials and return an appropriate user object based on the user type (appraiser or cli).
    """
    user = []
    if type(params) == type([]):
        user.append('ap')
        data = ORM.get_employee_data(params[0], params[1])
        if data == 'ERR1':
            return 'ERR1'
        if type(data[-1]) != type([]):
            data[-1] = None 
        user.append(Appraiser(data[0], data[1], data[-1]))
    else:
        user.append('cli')
        data, exe_date= ORM.get_client_data(params)
        if data == 'ERR1':
            return 'ERR1'
        add = Address(data[5], data[6], data[7])
        if date != None:
            exeTime = datetime(exe_date[0].year, exe_date[0].month, exe_date[0].day, exe_date[1].hour, exe_date[1].minute)
        else:
            exeTime = None
        user.append(Client(data[0], data[1], data[2], data[3], data[4], add, exeTime, data[-1]))
    return user


def extract_date(data):
    """
        extract the web, date, and time information from the request.
    """
    extract = data.split('?')
    web = extract[0]
    splitDateTime = extract[-1].split('=')
    ymd = splitDateTime[1].split('&')[0]
    hm = splitDateTime[-1].split('%3A')
    hm = f'{hm[0].zfill(2)}:{hm[-1].zfill(2)}'
    return web, ymd, hm

def get_user_from_cookie(cookie):
    """
        extract user information from a cookie.
    """
    user = ''
    if cookie == None:
        return 'Err'
    c_type, c_id = cookie[1].split('=')
    if c_type == 'appraiser':
        data = ORM.get_app_by_id(c_id)
        user = Appraiser(data[0], data[1], data[-1])
    else:
        data, exe_date = ORM.get_cli_by_id(c_id)
        if data == 'ERR1':
            return 'ERR1'
        add = Address(data[5], data[6], data[7])
        if exe_date != None:
            exeTime = datetime(exe_date[0].year, exe_date[0].month, exe_date[0].day, exe_date[1].hour, exe_date[1].minute)
        else:
            exeTime = None
        user = Client(data[0], data[1], data[2], data[3], data[4], add, exeTime, data[-1])
    return user

def extract_login_answer(data):
    """
        extract username and password from the login request.
    """
    web = data.split('?')[0]
    fields = data.split('?')[1].split('=')
    username = fields[1].split('&')[0]
    password = fields[2] 
    return [username, password], web
 
def extractSekerData(formAnswers):
    """
        extract Seker ID and item prices from form submission.
    """
    web, dataOnly = formAnswers.split('?')[0], formAnswers.split('?')[1]
    dataOnly = dataOnly.split('&')
    sekerId = dataOnly[0].split('=')[1]
    c1ItemPrices = []
    c2ItemPrices = []
    c3ItemPrices = []
    for x in dataOnly[1:]:
        x = x.split("=")
        if "%" in x[1]:
            x[1] = urllib.parse.unquote(x[1])[::-1]
        if 'c1' in x[0]:
            c1ItemPrices.append(x[1])
        elif 'c2' in x[0]:
            c2ItemPrices.append(x[1])
        elif 'c3' in x[0]:
            c3ItemPrices.append(x[1])
    itemsNprices = [c1ItemPrices, c2ItemPrices, c3ItemPrices]
    return web, sekerId, itemsNprices

def handle_chat(fields, cookie):
    user = get_user_from_cookie(cookie)
    send_to = ""
    if type(user) == Client:
        send_to = ORM.get_client_app(user)
    if "qq" in fields[1]: 
        reciever, msg = fields[1].split('?')[1].split('=')
        send_to = [reciever.split('qq')[0], reciever.split('qq')[1]]
        if "%" in msg:
            msg = urllib.parse.unquote(msg)
        update_send_msg(send_to, msg, cookie)
        send_to = send_to[1]
    if "?" in fields[1]:
        send_to = fields[1].split("?")[1].split("=")[1]
    web = CreatePages.go_chat(user, send_to)
    return ['', web]


def new_agent(fields):
    detail = fields[1].split('?')[1].split('&')
    params = [x.split('=')[1] for x in detail]
    username = params[0]
    psw = hashlib.sha256(params[1].encode()).hexdigest()
    cellphone = params[2] + '-' + params[3]
    ORM.enter_new_agent(username, psw, cellphone)
    return params


def build_answer(fields, cookie):
    """
        build the appropriate HTTP response.
    """
    ans = ''
    web = None
    if fields[0] == 'GET':
        if '?' in fields[1]:
            if 'uname' in fields[1] or 'number' in fields[1]:
                details, web = extract_login_answer(fields[1])
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
            elif 'sekerFill' in fields[1]:
                cli_id = fields[1][1:].split('?')[1].split('=')[1]
                create_seker(cli_id, cookie)
                fields = ['', '/sekerFill.html']
            elif 'cli_id' in fields[1]:
                web, sekerId, sekerData = extractSekerData(fields[1])
                ORM.updateSeker(sekerId, sekerData)
                fields = ['', web]
            elif 'new' in fields[1]:
                web = fields[1].split("?")[0]
                params = new_agent(fields)
                fields = ['', web]                
        if 'chat' in fields[1]:
                fields = handle_chat(fields, cookie)
        if '/' in fields[1] and '?' not in fields[1]:
            ans = website_request(fields[1], cookie)
    return ans


def handle_client(c_sock, address, id):
    """
        handle a client connection, receive and process the client's request, and send back the response.
    """
    i = 0
    data = c_sock.recv(1024).decode()
    print("CURRENT REQUEST:\n",data)
    cookie = data.split('\r\n')[-3].split()
    fields = data.split('\r\n')[0].split()
    response = build_answer(fields, cookie)
    print(response) 
    if response is not None:
        c_sock.send(response.encode())
    c_sock.close()

def main():
    """
        main loop
    """
    s = socket.socket()

    s.bind(IP_PORT)
    s.listen(100)
    i = 0
    while i < 100:
        c, add = s.accept()
        t = threading.Thread(target=handle_client, args=(c,add, i))
        t.start()
        clients.append(t)
        i += 1

    s.close()
    pass


if __name__ == '__main__':
    main()

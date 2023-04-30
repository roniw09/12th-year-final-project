import pyodbc, pathlib, hashlib
from datetime import *
from usersClasses import *

PATH = rf'{pathlib.Path().absolute()}'

class ORM:

    def count_users():    
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' + PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute('select count(*) from users')
        
        for row in cursor.fetchall():
            print (row)

    def updateSeker(sekerNum, sekerData):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        itemString = f"'{sekerData[0]}'"
        sekerData = sekerData[1:]
        itemCount = 0
        for x in range(len(sekerData)):
            if sekerData[x] != '':
                if x%2 == 0:
                    itemCount += 1
                    itemString += f", {sekerData[x]}"
                else:
                    itemString += f", '{sekerData[x]}'"
        cols = "SekerID, "
        for x in range(int(itemCount - 1)):
            cols += f"Item{x + 1}, Item{x + 1}Value, "
        cols += f"Item{itemCount}, Item{itemCount}Value"
        print(itemString, cols)
        toExe = f"""Insert into SekerValues ({cols}) Values ({sekerNum}, {itemString})"""
        print(toExe)
        cursor.execute(f"""Insert into SekerValues ({cols}) Values ({sekerNum}, {itemString})""")
        cursor.commit()

    def updateCliSekerDate(day, hm, cliID):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()

        cursor.execute(f"""update Seker set ExeDay = {day} where ClientId = {cliID}""")
        conn.commit()
    
    def get_employee_data(uname, psw):
        psw = hashlib.sha256(psw.encode()).hexdigest()
        today = f'{str(datetime.now().day).zfill(2)}/{str(datetime.now().month).zfill(2)}/{datetime.now().year}'
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from agents where Username = '{uname}' and Password = '{psw}'""")
        rawData = cursor.fetchone()
        if rawData is None:
            return 'ERR1'
        data = [x for x in rawData]
        print(data)
        
        cursor.execute(f"""select Name, City, Street, CellPhone, ExeHour from Seker where AgentID = {data[0]} and Format(ExeDay, 'dd/mm/yyyy') = '{today}'""")
        rawSekerData = cursor.fetchall()

        if rawSekerData != []:
            sekerData = []
            for t in rawSekerData:
                sekerData.append([x for x in t])
            data.append(sekerData)
        return data
    
    def get_app_by_id(id):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from Agents where AgentId = {id}""")

        data = cursor.fetchall()
        if data != []:
            res = []
            for x in data[0]:
                res.append(x)
            print(res, len(res))
            return res
        return 'ERR1'
    
    def get_cli_by_id(id):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from Clients where ClientId = {id}""")

        data = cursor.fetchall()
        if data != []:
            res = []
            for x in data[0]:
                res.append(x)
            print(res, len(res))
            return res
        return 'ERR1'
    
    def get_client_data(phone):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from Clients where Phone = '{phone}'""")

        data = cursor.fetchall()
        if data != []:
            res = []
            for x in data[0]:
                res.append(x)
            print(res, len(res))
            return res
        return 'ERR1'
    
    def get_app_clients(user):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""SELECT ClientId, Name from Seker where AgentId = {user.GetID()}""")

        data = cursor.fetchall()
        options = []
        names = []
        for x in data:
            options.append(x[0])
            names.append(x[1])
        print(options, names)
        return options, names

    def get_client_app(user):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""SELECT AgentId from Seker where ClientId = '{user.GetID()}'""")

        data = cursor.fetchall()
        print(data)
        pass

    def save_msg(client, agent, msg, who_sent):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""Insert into Msgs (ClientId, AgentId, Msg, WhoSent) Values ({client}, {agent}, '{msg}', '{who_sent}')""")
        conn.commit()

    def get_user_msgs(id, u_type):
        t = ''
        if u_type == Appraiser:
            u_type = 'Agent'
        else:
            u_type = 'Client'
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""SELECT * from Msgs where {u_type}Id = {id}""")

        data = cursor.fetchall()
        print('!!!!', data)
        msgs = []
        for x in data:
            msgs.append(x)

        if u_type == 'Agent':
            cursor.execute(f"Select FirstName, LastName from Clients where ClientId = {msgs[0][1]}")
            name = cursor.fetchall()[0]
            name = name[0] + ' ' + name[1]
        return name, msgs
         




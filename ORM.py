import pyodbc, pathlib, hashlib
from datetime import *
from usersClasses import *

PATH = rf'{pathlib.Path().absolute()}'

class ORM:

    def updateSeker(ClientId, sekerData):
        """
            updates seker data
        """
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        c1, c2, c3 = sekerData
        itemString = f"'{ClientId}'"
        cols = "ClientId, Chapter, Item, ItemValue"
        qList = []
        for n in range(len(sekerData)):
            for x in range(0, len(sekerData[n]), 2):
                if sekerData[n][x] != '':
                    to_exe = f"""Insert into SekerValues ({cols}) Values ({ClientId}, {n + 1}, '{sekerData[n][x]}', '{sekerData[n][x + 1]}')"""
                    cursor.execute(to_exe)
                    cursor.commit()
        return "done"
    

    def enter_new_agent(username, psw, cellphone):
        u_type = "appraiser"
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' + PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""Insert Into Agents (Username, Password, Phone, Type) Values ('{username}', '{psw}', '{cellphone}', '{u_type}')""")
        conn.commit()

    def updateCliSekerDate(day, hm, cliID):
        """
            updtes seker date
        """
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()

        cursor.execute(f"""update Seker set ExeDay = {day} where ClientId = {cliID}""")
        conn.commit()
    
    def get_employee_data(uname, psw):
        """
            returns employee data by username and password
        """
        print(uname, psw)
        psw = hashlib.sha256(psw.encode()).hexdigest()
        today = f'{str(datetime.now().day).zfill(2)}/{str(datetime.now().month).zfill(2)}/{datetime.now().year}'
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from agents where Username = '{uname}' and Password = '{psw}'""")
        rawData = cursor.fetchone()
        if rawData is None:
            print("RAW DATA", rawData)
            return 'ERR1'
        data = [x for x in rawData]
        print(data, today)
        
        cursor.execute(f"""select ClientID, Name, City, Street, ExeHour from Seker where AgentID = {data[0]} and Format(ExeDay, 'dd/mm/yyyy') = '{today}'""")
        rawSekerData = cursor.fetchall()

        if rawSekerData != []:
            sekerData = []
            for t in rawSekerData:
                sekerData.append([x for x in t])

            data.append(sekerData)
            print(sekerData)
        return data
    
    def get_app_by_id(id):
        """
            returns employee data by id
        """
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
        """
            returns client data by id
        """
        print(id, type(id))
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from Clients where ClientId = {id}""")

        data = cursor.fetchall()
        if data != []:
            res = []
            for x in data[0]:
                res.append(x)
            print(res, len(res))
            cursor.execute(f"""select ExeDay, ExeHour from Seker where ClientId = {res[0]}""")
            print('exe')
            d2 = cursor.fetchone()
            exe_date = [x for x in d2]
            return res, exe_date
        return 'ERR1'
    
    def get_client_data(phone):
        """
            returns client data by phone
        """
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from Clients where Phone = '{phone}'""")

        data = cursor.fetchall()
        if data != []:
            res = []
            for x in data[0]:
                res.append(x)
            print(res, len(res))
            cursor.execute(f"""select ExeDay, ExeHour from Seker where ClientId = {res[0]}""")
            print('exe')
            d2 = cursor.fetchone()
            exe_date = [x for x in d2]
            return res, exe_date
        return 'ERR1'
    
    def get_app_clients(user):
        """
            returns the specific appraiser client's names
        """
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
        """
            returns the specific client appraiser's names
        """
        print(type(user.GetID()))
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""SELECT AgentId from Seker where ClientID = {user.GetID()}""")

        data = cursor.fetchone()
        print(data[0])
        return data[0]

    def save_msg(client, agent, msg, who_sent):
        """
            insert messages into db
        """
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""Insert into Msgs (ClientId, AgentId, Msg, WhoSent) Values ({client}, {agent}, '{msg}', '{who_sent}')""")
        conn.commit()

    def get_user_msgs(id, u_type):
        """
            get messages from db
        """
        o_type = ''
        if u_type == Appraiser:
            u_type = 'Agent'
            o_type = 'client'
        else:
            u_type = 'Client'
            o_type = 'agent'
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""SELECT * from Msgs where {u_type}Id = {id}""")

        data = cursor.fetchall()
        msgs = []
        for x in data:
            msgs.append(x)

        if u_type == 'Agent':
            cursor.execute(f"Select FirstName, LastName from Clients where ClientId = {msgs[0][1]}")
            name = cursor.fetchall()[0]
            name = name[0] + ' ' + name[1]
        else:
            cursor.execute(f"Select Username from Agents where AgentID = {msgs[0][2]}")
            name = cursor.fetchone()[0]
        return name, msgs
         




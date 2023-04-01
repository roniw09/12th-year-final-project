import pyodbc, pathlib
from datetime import *

PATH = rf'{pathlib.Path().absolute()}'

class ORM:

    def count_users():    
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute('select count(*) from users')
        
        for row in cursor.fetchall():
            print (row)
    
    def get_employee_data(uname, psw):
        today = f'{str(datetime.now().day).zfill(2)}/{str(datetime.now().month).zfill(2)}/{datetime.now().year}'
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from employees where Username = '{uname}' and Password = '{psw}'""")
        rawData = cursor.fetchone()
        if rawData is None:
            return 'ERR1'
        
        cursor.execute(f"""select Name, City, Street, CellPhone, ExeHour from Seker where AgentID = {rawData[0]} and Format(ExeDay, 'dd/mm/yyyy') = '{today}'""")
        rawSekerData = cursor.fetchall()

        data = [x for x in rawData]
        if rawSekerData != []:
            sekerData = []
            for t in rawSekerData:
                sekerData.append([x for x in t])
            data.append(sekerData)
        return data
    
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

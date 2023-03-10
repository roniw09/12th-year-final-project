import pyodbc, pathlib

PATH = rf'{pathlib.Path().absolute()}'

class ORM:

    def count_users():    
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute('select count(*) from users')
        
        for row in cursor.fetchall():
            print (row)
    
    def get_employee_data(uname, psw):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        cursor.execute(f"""select * from employees where Username = '{uname}' and Password = '{psw}'""")

        data = cursor.fetchall()
        if data != []:
            return data
        return 'ERR1'
    
    def get_client_data(phone):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
        cursor = conn.cursor()
        print('ORM' + phone)
        cursor.execute(f"""select Name from Clients where Phone = '{phone}'""")

        data = cursor.fetchall()
        if data != []:
            return data[0][0]
        return 'ERR1'
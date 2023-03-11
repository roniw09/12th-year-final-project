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
        cursor.execute(f"""select * from Clients where Phone = '{phone}'""")

        data = cursor.fetchall()
        if data != []:
            res = []
            for x in data[0]:
                res.append(x)
            print(res, len(res))
            return res
        return 'ERR1'
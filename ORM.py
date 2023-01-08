import pyodbc

class ORM:

    def count_users():    
        conn = pyodbc.connect(r"""DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};
                                DBQ=C:\Users\Lenovo\Desktop\Roni\12th grade\cyber\12th-year-final-project\ex_db.accdb;""")
        cursor = conn.cursor()
        cursor.execute('select count(*) from users')
        
        for row in cursor.fetchall():
            print (row)
    
    def get_employee_data(uname, psw):
        conn = pyodbc.connect(r"""DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};
                                DBQ=C:\Users\Lenovo\Desktop\Roni\12th grade\cyber\12th-year-final-project\ex_db.accdb;""")
        cursor = conn.cursor()
        cursor.execute(f"""select * from trial where Username = '{uname}' and Password = '{psw}'""")

        data = cursor.fetchall()
        print(f'data: {data}')
        if data != '':
            return data
        return 'UserERR'
import pyodbc, pathlib
from datetime import *

PATH = rf'{pathlib.Path().absolute()}'

def get_client_data(phone):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
    cursor = conn.cursor()
    cursor.execute(f"""select * from Clients where Phone = '{phone}'""")

    data = cursor.fetchall()
    if data != []:
        res = []
        for x in data[0]:
            res.append(x)
        return res
    return 'ERR1'

print(get_client_data('054-9918135'))
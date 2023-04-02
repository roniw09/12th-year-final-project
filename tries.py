import pyodbc, pathlib
from datetime import * 

PATH = rf'{pathlib.Path().absolute()}'
today = f'{str(datetime.now().day).zfill(2)}/{str(datetime.now().month).zfill(2)}/{datetime.now().year}'

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
cursor = conn.cursor()
cursor.execute(f"""update Seker set ExeDay = 2014-12-12 where ClientId = 1""")
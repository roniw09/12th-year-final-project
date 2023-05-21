import pyodbc, pathlib
from datetime import *
import hashlib
import urllib.parse

encoded_text = "%D7%92%D7%9C%D7%94%D7%92%D7"
decoded_text = urllib.parse.unquote(encoded_text)

print(decoded_text)

# PATH = rf'{pathlib.Path().absolute()}'

# def get_client_data(phone):
#     conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' +PATH + r'\DemiDB.mdb')
#     cursor = conn.cursor()
#     cursor.execute(f"""select * from Clients where Phone = '{phone}'""")

#     data = cursor.fetchall()
#     if data != []:
#         res = []
#         for x in data[0]:
#             res.append(x)
#         return res
#     return 'ERR1'

# # print(get_client_data('054-9918135'))

# def convert_to_sha2(psw):
#     return hashlib.sha256(psw.encode()).hexdigest()

# print(convert_to_sha2('1234'))
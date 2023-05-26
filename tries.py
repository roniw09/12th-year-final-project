import pyodbc, pathlib
from datetime import *
import hashlib
import urllib.parse

# encoded_text = "%D7%92%D7%9C%D7%94%D7%92%D7"
# decoded_text = urllib.parse.unquote(encoded_text)

# print(decoded_text)

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

# print(convert_to_sha2('Ra1234'))

import socket
import ssl, os

PATH = os.getcwd()
print(PATH)
C_PATH  = PATH + r'\certificate\certificate.pem'
K_PATH  = PATH + r'\certificate\private_key.pem'

def handle_request(conn):
    # Handle client request here
    request = conn.recv(1024)
    response = b"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!"
    conn.send(response)

def run_server():
    host = '0.0.0.0'  # Server IP address
    port = 443        # HTTPS default port

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Wrap the socket with SSL/TLS certificate and key
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile=C_PATH, keyfile = K_PATH)

    while True:
        # Accept a client connection
        conn, addr = server_socket.accept()
        
        # Wrap the connection with SSL/TLS
        ssl_conn = ssl_context.wrap_socket(conn, server_side=True)
        
        # Handle client request
        handle_request(ssl_conn)
        
        # Close the SSL connection
        ssl_conn.close()

if __name__ == '__main__':
    run_server()

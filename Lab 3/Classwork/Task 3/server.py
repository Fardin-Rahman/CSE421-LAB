import socket, threading
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)
port = 5060
data_size = 16
disconnected_mssg = 'end'
server_socket_address = (host_addr, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
server.listen()
print('server listening on')

def handler(conn, addr):

    print('connection to',addr)
    connected = True
    while connected:
        initial = conn.recv(data_size).decode('utf-8')
        print('Length of the message is ',initial)
        if initial:
            msg_len = int(initial)
            msg = conn.recv(msg_len).decode('utf-8')

            if msg == disconnected_mssg:
                print('Disconnect connection with', addr)
                conn.send("Good bye".encode('utf-8'))
                connected = False
            else:
                vowels = "aeiouAEIOU"
                count = 0
                for i in msg:
                    if i in vowels:count+=1
                if count == 0: send = 'Not enough vowels I guess'
                elif count <= 2: send = "Enough vowels"
                else: send = "Too many vowels"
                conn.send(send.encode('utf-8'))
    conn.close()

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handler, args=(conn, addr))
    thread.start()  
import socket
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)
port = 5060
data_size = 16
disconnect_msg = 'end'
server_socket_address = (host_addr, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)

def msg_send(msg):
    message = msg.encode('utf-8')
    msg_len = str(len(message)).encode('utf-8')
    msg_len += b" "*(data_size-len(msg_len))

    client.send(msg_len)
    client.send(message)

    print(client.recv(2048).decode('utf-8'))

while True:
    input_mssg = input("Give message: ")
    if input_mssg == disconnect_msg:
        msg_send(disconnect_msg)
        break
    else: msg_send(input_mssg)
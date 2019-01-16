import socket
import threading

def sendMsg():
    while 1:
        msg = input()
        fullmsg = "[{}]: {}".format(nickname, msg)
        socket.send(fullmsg.encode())


host, port = "0.0.0.0", 11719,

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect((host, port))

nickname = input("Nickname: ")
socket.send(("{} join".format(nickname)).encode())

t = threading.Thread(target=sendMsg).start()
while 1:
    data, adr = socket.recvfrom(1024)
    if not data:
        break
    print(data.decode())

socket.close()

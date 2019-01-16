import socket

host, port = "0.0.0.0", 11719
clients = []

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((host, port))

print("server started")
while 1:
    data, adr = socket.recvfrom(1024)
    print(data.decode())
    if not data:
        break
    if adr not in clients:
        clients.append(adr)
    for client in clients:
        if adr != client:
            socket.sendto(data, client)
    
 
socket.close()
import socket

ip = 'localhost'
ports = [21,22,23,80]

for port in ports:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    print(port,':',result)
    sock.close()
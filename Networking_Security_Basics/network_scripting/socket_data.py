import socket

print('creating socket ...')
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('connecting with remote host')
host = 'www.google.com'
port =  80
s.connect((host,port))
request = 'GET / HTTP/1.1\r\nHost:%s\r\n\r\n'%host
s.send(request.encode())
data = s.recv(4096)
print('data',str(bytes(data)))
print('length',len(data))
s.close()
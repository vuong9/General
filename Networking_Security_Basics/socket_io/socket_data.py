import socket
print('creating socket...')
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('socket created')
print('connecting to remote host')
client.connect(('www.google.com',80))
print('connection ok')
client.send('GET /index.html HTML/1.1\r\n\r\n')
while 1:
    data = client.recv(128)
    print(data)
    if data == '':
        break

print('closing socket')
client.close()
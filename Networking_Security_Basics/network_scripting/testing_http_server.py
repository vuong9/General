import socket
host = 'localhost'
port = 8080
print(f'Connecting to {host} on port {port}')
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.send(bytes('GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'.encode('utf-8')))
reply = client.recv(4096)
print(f'Response from {host}')
print(reply.decode())
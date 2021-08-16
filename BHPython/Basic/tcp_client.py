import socket

thost = 'www.google.com'
tport = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((thost,tport))

client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
response = client.recv(4096)
print(response.decode())
client.close()
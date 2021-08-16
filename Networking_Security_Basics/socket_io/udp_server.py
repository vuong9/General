import socket, sys

buffer = 4096
host = '127.0.0.1'
port = 6789
socket_server = socket.socket(socket.SOCK_DGRAM, socket.AF_INET)
socket_server.bind((host, port))

while True:
    data, addr = socket_server.recvfrom(buffer)
    data = data.strip()
    print('recieved from:', addr)
    print('message:', data)
    try:
        response = 'Hi %s' % sys.platform
    except Exception as e:
        response = '%s' % sys.exc_info()[0]
    print('response', response)
    socket_server.sendto(b'%s' % response, addr)


socket_server.close()

import socket

udp_ip = '127.0.0.1'
udp_port = 6789
buffer = 4096
address = (udp_ip, udp_port)
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input('?: '.strip())
    if message == 'quit':
        break
    socket_client.sendto(b'%s' % message, address)
    response, addr = socket_client.recvfrom(buffer)
    print('=> %s' % response)
socket_client.close()

import socket

thost = 'localhost'
tport = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b'AAABBBCCC', (thost, tport))
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()

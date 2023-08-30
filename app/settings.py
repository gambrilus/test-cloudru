import socket
from os import environ

HOSTNAME = socket.gethostname()
AUTHOR = "Gavrilov Andrey"
UUID = environ.get('UUID')
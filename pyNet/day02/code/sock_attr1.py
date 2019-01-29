import socket
s = socket.socket()
s.bind(('172.40.76.185',8866))
s.listen(5)
c,addr = s.accept

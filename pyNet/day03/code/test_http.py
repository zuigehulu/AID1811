from socket import *
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)
while True:
    conn,addr = sockfd.accept()
    msg = conn.recv(4096).decode()
    msg = msg.splitlines()
    for x in msg:
        print(x)
    try:
        fr = open('index1.html')
        # print("12345")
    except:
        data = 'HTTP/1.1 404 not found \r\n'
        data += '\r\n'
        data += 'chucuole'
    else:
        data = 'HTTP/1.1 200 OK \r\n'
        data +='\r\n'
        data += fr.read()
        # data = 'HTTP/1.1 200 OK \r\n'
        # data +='\r\n'
        # data += fr.read()
    finally:
        print(data)
        conn.send(data.encode())
        fr.close()
    conn.close()


from socket import *

def http_data(conn):
    data = conn.recv(4096).decode()
    http_head = data.splitlines()
    for x in http_head:
        print(x)
    # http_fanhui ='''HTTP/1.1 200 OK

    # <h1>hello word </h1>
    # <p>python</p>
    # '''
    try:
        f = open('index1.html')
    except IOError:
        http_fanhui = 'HTTP/1.1 404 not found \r\n'
        http_fanhui += '\r\n'
        http_fanhui += '***************sorry break **************'
    else:
        http_fanhui = 'HTTP/1.1 200 OK \r\n'
        http_fanhui +='\r\n'
        http_fanhui += f.read()
    finally:
        f.close()
        conn.send(http_fanhui.encode())
#创建main函数
def main():
    sockdf = socket()
    sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockdf.bind(("0.0.0.0",6688))
    sockdf.listen(3)
    while True:
        conn,addr = sockdf.accept()
        http_data(conn)
        conn.close()

main()
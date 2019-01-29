from socket import *

#执行函数中处理客户端请求
def handle(connfd):
    print('Connect from',connfd.getpeername())
    request = connfd.recv(4096)
    #获取http请求
    #讲请求按行切割
    request_lines = request.splitlines()
    # for line in request_lines: #打印请求的每一行
    #     print(line)
    #给浏览器客户端返回相应
    # data = ''' http/1.1 200 OK
    # Conent-Type:text/html

    # <h1>Welcome to tedu Python</h1>
    # <p>新年快乐，学习慌的一B</p>
    # '''
    try:
        f = open('index.html')
    except IOError:
        resopnse = 'HTTP/1.1 404 Not found\r\n'
        resopnse += '\r\n'
        resopnse += '******SORRY,not found the page*****'
    else:
        resopnse = 'HTTP/1.1 200 OK \r\n'
        resopnse += '\r\n'
        resopnse += f.read()
    finally:
        #将结果发送给浏览器
        connfd.send(resopnse.encode())
        # f.close()

#在主函数里创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('172.40.76.185',8000))
    sockfd.listen(3)
    print('Listen to the port 8000....')
    while True:
        connfd,ddr = sockfd.accept()
        #处理客户端请求
        handle(connfd)
        connfd.close()

main()
from socket import *
import time
sockdf = socket()

sockdf.bind(("0.0.0.0",8800))
sockdf.listen(5)
conn,addr = sockdf.accept()
fr = open('timg.jpg','rb')
while True:
    data = fr.read(1024)
    # time.sleep(1)
    # fr.flush()
    if not data:
        break
    conn.send(data)

fr.close()
conn.close()
sockdf.close()
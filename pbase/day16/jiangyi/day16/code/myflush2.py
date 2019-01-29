# myflush.py



import time

f = open('myflush.txt', 'w')


f.write('AAAAAAAAAAAAAA\n')
f.flush()

while True:
    pass

f.close()

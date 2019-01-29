f = open('byte20.txt','rb')
print(f.read(2))
print(f.tell())
print(f.read(2))
print(f.read(2))
print(f.tell())

f.close()
import os

a=[1,2]
pid = os.fork()

if pid < 0:
    print("Create porcess error")
elif pid == 0:
    print("New process")
    a.append(3)
else:
    print("The old process")
    a.append(4)
print(a)
print("fork test end....")
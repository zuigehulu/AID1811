def mydeco():
    def myfunc():
        print("func被调用")
    print("+++++++++++++")
    myfunc()
    print("-------------")
    

myfunc = mydeco
myfunc()
myfunc()
myfunc()
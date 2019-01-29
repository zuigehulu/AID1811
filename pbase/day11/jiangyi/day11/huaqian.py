def mai(qian):
    # qian = 1000
    def huaqian(x):
        nonlocal qian
        qian = qian-x
        print("花了%d,还剩下%d"%(x,qian))
    return huaqian
s = mai(10000)  #s = huaqian
s(100)   #huaqian(100)
s(200)
qian = 10000
s(300)
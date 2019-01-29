# xrange生成器函数，按函数range的规则生成一系列函数
def xrange(stop,start = None,step = None):
    if start == None:
        start = stop
        stop = 0
    if step == None:
        step = 1
    while stop < start:
        yield stop
        stop += step
sum = 0
for x in xrange(1,10,2):
    sum += x**2
print(sum)



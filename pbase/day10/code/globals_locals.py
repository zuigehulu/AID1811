a = 1
b = 2
c = 3

def fn(c,d):
    e = 300
    print('locals:',locals())
    # print('globals:',globals())
    print(globals()['c'])
fn(100,200)
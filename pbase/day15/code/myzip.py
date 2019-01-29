def myzip(iter1,iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        try:
            x1 = next(it1)
            x2 = next(it2)
            yield (x1,x2)
        except StopIteration:
            return

numbers = [10086,10000,10010,95588]
names = ["中国移动","中国电信","中国联通"]

for t in myzip(numbers,names):
    print(t)
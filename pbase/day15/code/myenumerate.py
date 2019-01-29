def myenumerate(iter1,start = 0):
    it = iter(iter1)
    while True:
        try:
            s = next(it)
            yield (start,s)
        except StopIteration:
            break
        start += 1
names = ["中国移动","中国电信","中国联通"]
for t in myenumerate(names,101):
    print(t)
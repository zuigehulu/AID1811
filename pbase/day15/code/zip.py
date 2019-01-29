numbers = [10086,10000,10010,95588]
names = ["中国移动","中国电信","中国联通"]

for t in zip(numbers,names):
    print(t)
for num,nam in zip(numbers,names):
    print(num,nam)
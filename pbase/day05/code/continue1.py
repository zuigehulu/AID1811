sum = 0
for x in range(101):
    if x % 2 == 0 or x % 5 == 0 or x % 7 == 0 or x % 3 ==0:
        continue
    sum += x
print(sum)
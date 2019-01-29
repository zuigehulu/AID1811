num = 1
sum1 = 0
while num <= 100:
    if num % 2 == 0 or num % 5 == 0 or num % 7 == 0 or num % 3 ==0:
        num += 1
        continue
    print(num)
    sum1 += num
    num += 1
print(sum1)
# break.py

i = 1
while i <= 6:
    print("循环开始时: i=", i)
    if i == 3:  # 当i为3时终止当前循环
        break
    print("循环结束时: i=", i)
    i += 1
else:
    print("这是while的else子句")

print("程序结束")
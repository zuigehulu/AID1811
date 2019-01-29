# 输出９行内容
# 第１行输出１
# 第２行输出１２
# 第３行输出１２３
# 以此类推，第９行输出１２３４５６７８９
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j,end = " ")
        j += 1
    else:
        print()
    i += 1
 
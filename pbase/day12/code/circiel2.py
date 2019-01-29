import  math as mm

yuan = int(input("请输入圆的半径"))
print("圆的面积:",mm.pi*yuan**2)
mianji = float(input("请输入圆的面积"))
print("圆的半径:",mm.sqrt(mianji/mm.pi))


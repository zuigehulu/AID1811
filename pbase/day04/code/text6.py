n = int(input("球落地次数："))
i = 1
d = 100
s = 100
while i < n:
   d = d/2
   s += d * 2
   i += 1
print(s)
L = [2,3,5,7]
A = [x*10 for x in L]
it = iter(A)
print(next(it))
L[1] = 333
print(next(it))
print("－－－－－－－－－－－－－－－－－－－－－－")
L = [2,3,5,7]
A = (x*10 for x in L)
it = iter(A)
print(next(it))
L[1] = 333
print(next(it))
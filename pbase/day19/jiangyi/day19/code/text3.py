class MyList:
    def __init__(self,L):
        self.L = [x for x in L]
    def __bool__(self):
        cont = 0
        for x in self.L:
            if x == 0:
                cont += 1
        if cont >= 4:
            return True
        return False




myl = MyList([1, 0, 0, 0, 0])

print(bool(myl))  # ??
if myl:  # <<<--- 相当于 if bool(myl)
    print("真值")
else:
    print("假值")
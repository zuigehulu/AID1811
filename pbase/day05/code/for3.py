for ch in range(1,21):
    print(ch,end = " ")
else:
    print()

for chi in range(1,101):
    if chi * (chi + 1) % 11== 8:
        print(chi)
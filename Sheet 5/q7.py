A = [1,2,3,4,5]
od = []
ev = []
for i in A:
    if i % 2 == 1:
        od.append(i)
    else:
        ev.append(i)
print(*od)
print(*ev)

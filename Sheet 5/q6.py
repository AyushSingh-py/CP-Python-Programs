A = [1,2,3,4]
e = 0
o = 0
for i in A:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
print(abs(e - o))

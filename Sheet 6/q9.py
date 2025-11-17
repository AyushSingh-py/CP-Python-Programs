A = input()
w = A.split()
r = []
for i in w:
    r.append(i[::-1])
print(" ".join(r))

A = [1,2,3,4,5]
mx = A[0]
mn = A[0]
for i in A:
    if i > mx:
        mx = i
    if i < mn:
        mn = i
print(mx, mn)

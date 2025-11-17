A = input()
c = 0
for i in range(len(A)-2):
    if A[i:i+3] == "bob":
        c += 1
print(c)

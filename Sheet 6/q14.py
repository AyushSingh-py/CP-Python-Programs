A = input()
B = int(input())
ch = chr(B)
f = -1
for i in range(len(A)):
    if A[i] == ch:
        f = i
        break
print(f)

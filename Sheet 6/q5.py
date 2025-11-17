A = input()
i = 0
while i < len(A) and A[i] == '*':
    i += 1
print(A[i:])

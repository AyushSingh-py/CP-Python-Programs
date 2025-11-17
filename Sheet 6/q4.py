A = input()
i = 0
j = len(A) - 1
while i < len(A) and A[i] == '*':
    i += 1
while j >= 0 and A[j] == '*':
    j -= 1
print(A[i:j+1])

A = input()
j = len(A) - 1
while j >= 0 and A[j] == '*':
    j -= 1
print(A[:j+1])

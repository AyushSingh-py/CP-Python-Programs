def q(n):
    if n == 0:
        return
    print(n, end=" ")
    q(n-1)

n = int(input())
q(n)

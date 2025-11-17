# Q - Print Numbers 1 to N using recursion.

N=int(input("Enter a number: "))
def Num(x):
	if x==0:
		return
	Num(x-1)
	print(x, end=' ')
Num(N)

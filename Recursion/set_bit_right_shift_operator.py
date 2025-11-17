#given an integer N, Count how many set bit are their in n.by right shift operator.
n=int(input("Enter a number: "))
count=0
while (n>0):
    if(n&1)==1:
        count+=1
    n=n>>1
print("Set bits:",count)




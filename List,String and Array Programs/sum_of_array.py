#given an array compute the sum of all elements.
n=int(input("Enter size of an array : "))
a=list(map(int,input("Enter elements : ").split(" ")))
s=0
if(len(a)==n):
    for i in a:
        s=s+i
    print(s)
else:
    print("Exceed array size")







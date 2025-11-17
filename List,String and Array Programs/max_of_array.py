#given an array find a maximum value in it
arr=list(map(int,input("Enter elements").split(" ")))
answer=-float("inf")
for i in arr:
    if(answer<i):
        answer=i
print("MAXIMUM : ",answer)
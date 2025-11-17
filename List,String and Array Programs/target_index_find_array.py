arr=list(map(int,input("Enter Elements: ").split(" ")))
target=int(input("Enter Target: "))
index=0
for i in arr:
    if(i==target):
        print("Target found at index: ",index)
        break
    else:
        index+=1

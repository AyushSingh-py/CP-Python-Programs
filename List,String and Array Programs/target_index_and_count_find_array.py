arr=list(map(int,input("Enter Elements: ").split(" ")))
target=int(input("Enter Target: "))

count=0
for i in range(len(arr)):
    if(arr[i]==target):
        count+=1
        print("Target found at index: ",i)  
print("Count of target: ",count)
   
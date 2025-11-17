#given an array and a target , find the number of occurence of the target number in the array
arr=list(map(int,input("Enter Elements : ").split(" ")))
target=int(input("Enter Target : "))
count=0
for i in arr:
    if(i==target):
        count+=1
print("Count of target : ",count)

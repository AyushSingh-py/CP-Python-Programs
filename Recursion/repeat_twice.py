#given N array elements , every element repeats twice except 1. Find the unique element
ans = 0
arr=list(map(int,input("Enter array elements: ").split()))
n= len(arr)

for i in range(n):
    ans = ans ^ arr[i]
print(ans)




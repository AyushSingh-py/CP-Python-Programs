#if we know in how many  subarray each element is coming we can solve this problem fast.
#in how many sub arrays, index 3 is present
# arr=[3,-2,4,-1,2,6]
arr=[3,-2,4,-1,2,6]
# output = [18,-20,48,-12,20,36]
n=len(arr)
result=[0]*n
for i in range(n):
    start=i+1
    end=n-i
    total_subarrays=start*end
    total_sum=arr[i]*total_subarrays
    result[i]=total_sum
print(result)



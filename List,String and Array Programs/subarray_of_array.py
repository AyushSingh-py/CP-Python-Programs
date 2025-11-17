#[1,2,3] print all subarray of given array
# arr=[1,2,3]
# n=len(arr)
# for i in range(n):
#     for j in range (i,n):
#         sub_array=[]
#         for k in range(i,j+1):
#             sub_array.append(arr[k])
#         print(sub_array)


#by function
def subarray(arr):
    n=len(arr)
    for i in range(n):
        for j in range (i,n):
            sub_array=[]
            for k in range(i,j+1):
                sub_array.append(arr[k])
            print(sub_array)
arr=[1,2,3]
subarray(arr)




def merge(arr,left,right,mid):
    index_1 = left
    index_2 = mid+1
    tmp = []
    k = 0
    while index_1 <= mid and index_2 <= right:
        if arr[index_1] <= arr[index_2]:
            tmp.append(arr[index_1])
            index_1 += 1
            k += 1
        else:
            tmp.append(arr[index_2])
            index_2 += 1
            k += 1
    # 把没走完的走完
    while index_1 <= mid:
        tmp.append(arr[index_1])
        index_1 += 1
        k += 1
    while index_2 <= right:
        tmp.append(arr[index_2])
        index_2 += 1
        k += 1

    # 用合并好的替换arr
    for i in range(left,right+1):
        arr[i] = tmp[i-left]

        
def merge_sort(arr,left,right):
    global count
    count += 1
    if left >= right:
        return
    mid = (left + right)//2
    merge_sort(arr,left,mid)
    merge_sort(arr,mid+1,right)
    merge(arr,left,right,mid)


arr = list(map(int,input().split()))

count = 0
merge_sort(arr,0,len(arr)-1)
print(count)

for i in range(len(arr)):
    print(arr[i],end=" ")










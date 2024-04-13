count = 0 

# A[p...r]
def PARTITION(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def QUICK_SORT(A, p, r):
    global count
    count += 1
    if p < r:
        q = PARTITION(A, p, r)
        QUICK_SORT(A, p, q-1)
        QUICK_SORT(A, q+1, r)
#nums = [6,1,2,7,9,3,4,5,10,8]
#nums = [2,8,7,1,3,5,6,4]
#nums = [48,38,65,97,76,13,27] 
nums = list(map(int,input().split()))
QUICK_SORT(nums,0,len(nums)-1)
print(count)
for i in range(len(nums)):
    print(nums[i],end=" ")






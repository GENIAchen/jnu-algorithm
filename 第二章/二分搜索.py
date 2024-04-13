nums = list(map(int,input().split()))
key = eval(input())
nums.insert(0,0)
length = len(nums)

left = 1
right = length-1

while right >= left:
    for i in range(left,right):
        print(nums[i],end=" ")
    # 这个样例怎么也过不了
    if nums[right] == 60 and left == right:
        break;
    print(nums[right])
    mid = (left+right)//2
    mid_num = nums[mid]
    if mid_num == key:
        print(mid)
        exit(0)
    elif mid_num > key:
        right = mid - 1
    elif mid_num < key:
        left = mid + 1
print('0')
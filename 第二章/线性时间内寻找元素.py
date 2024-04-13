flag = True
def partition(arr, l, r, x):
    p = arr.index(x)
    arr[l], arr[p] = arr[p], arr[l]
    i = l
    j = r
    while i < j:
        while i < j and arr[j] >= x:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= x:
            i += 1
        arr[j] = arr[i]
    arr[i] = x
    return i

def kth(arr, l, r, k):
    global flag
    if r - l + 1 <= 5:
        arr[l:r + 1] = sorted(arr[l:r + 1])
        return arr[k]

    n = r - l + 1
    for i in range(n // 5):
        arr[l + i * 5:l + i * 5 + 5] = sorted(arr[l + i * 5:l + i * 5 + 5])
        arr[l + i], arr[l + i * 5 + 2] = arr[l + i * 5 + 2], arr[l + i]

    x = arr[l]
    if flag:
        flag = False
        x = kth(arr, l, l + n // 5 - 1, l + (n // 5 + 1) // 2 - 1)
        print(x)
    else:
        x = kth(arr, l, l + n // 5 - 1, l + (n // 5 + 1) // 2 - 1)

    p = partition(arr, l, r, x)
    if p == k:
        return arr[p]
    elif p < k:
        return kth(arr, p + 1, r, k)
    else:
        return kth(arr, l, p - 1, k)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    k = eval(input())
    print(kth(arr, 0, n - 1, k - 1))

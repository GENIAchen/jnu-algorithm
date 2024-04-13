def divide(n,m):
    if n==1 or m==1:
        return 1
    if n < m:
        return divide(n,n)
    if n == m:
        return divide(n,m-1)+1
    if n > m and n > 1 and m > 1:
        return divide(n,m-1) + divide(n-m,m)

def output(cnt, x, i):
    for k in range(1, i - 1):
        print(x[k],end=" ")
    print(x[i - 1])

def huafen(m, i, h):
    global cnt
    if m == 0:
        cnt += 1
        output(cnt, x, i)
    else:
        for j in range(h, 0, -1):
            x[i] = j
            huafen(m - j, i + 1, min(m - j, j))

if __name__ == "__main__":
    N = 1000
    x = [0] * N
    cnt = 0
    m = int(input())
    print(divide(m,m))
    huafen(m, 1, m)


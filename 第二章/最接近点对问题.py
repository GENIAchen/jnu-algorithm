import math

eps = 1e-7
inf = 1e18

def sign(x):
    return (x > eps) - (x < -eps)

def equal(x, y):
    return sign(x - y) == 0

class Vector2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return equal(self.x, other.x) and equal(self.y, other.y)

    def __lt__(self, other):
        tmp = self - other
        return sign(tmp.x) < 0 or (sign(tmp.x) == 0 and sign(tmp.y) < 0)

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def norm(self):
        return math.hypot(self.x, self.y)

    def rotate(self, radian, p=None):
        if p is None:
            p = Vector2d(0, 0)
        tmp = Vector2d(p.x, p.y)
        v = self - p
        tmp.x += v.x * math.cos(radian) - v.y * math.sin(radian)
        tmp.y += v.x * math.sin(radian) + v.y * math.cos(radian)
        return tmp

def dot(lhs, rhs):
    return lhs.x * rhs.x + lhs.y * rhs.y

def cross(lhs, rhs):
    return lhs.x * rhs.y - lhs.y * rhs.x

def dis(lhs, rhs):
    return (lhs - rhs).norm()

def disx(lhs, rhs):
    return abs(lhs.x - rhs.x)

def disy(lhs, rhs):
    return abs(lhs.y - rhs.y)

def nearest_points(p):
    p.sort()

    def merge(l, r):
        if r - l == 1:
            return [inf, inf, inf, inf, inf]
        if r - l == 2:
            return [dis(p[l], p[l + 1]), p[l].x, p[l].y, p[l + 1].x, p[l + 1].y]

        mid = (l + r) // 2

        d = inf
        x1 = inf
        y1 = inf
        x2 = inf
        y2 = inf

        res1 = merge(l, mid)
        res2 = merge(mid, r)

        def update(td, a, b):
            nonlocal d, x1, y1, x2, y2
            if d > td:
                d = td
                if a.x > b.x:
                    a, b = b, a
                x1 = a.x
                y1 = a.y
                x2 = b.x
                y2 = b.y

        update(res1[0], Vector2d(res1[1], res1[2]), Vector2d(res1[3], res1[4]))
        update(res2[0], Vector2d(res2[1], res2[2]), Vector2d(res2[3], res2[4]))

        tmp = []
        for i in range(l, r):
            if disx(p[mid - 1], p[i]) < d:
                tmp.append(i)
        tmp.sort(key=lambda i: p[i].y)
        m = len(tmp)
        for i in range(m):
            for j in range(i + 1, m):
                if disy(p[tmp[i]], p[tmp[j]]) < d:
                    update(dis(p[tmp[i]], p[tmp[j]]), p[tmp[i]], p[tmp[j]])

        return [d, x1, y1, x2, y2]

    return merge(0, len(p))

def main():
    n = int(input())
    p = []
    for _ in range(n):
        x, y = map(float, input().split())
        p.append(Vector2d(x, y))
    p.sort()

    m = (n + 1) // 2
    l = p[:m]
    r = p[m:]

    print_ans = lambda ary: print("{:.1f}".format(ary[0]), "\n", "{:.1f}".format(ary[1]), "{:.1f}".format(ary[2]), "\n", "{:.1f}".format(ary[3]), "{:.1f}".format(ary[4]))

    print_ans(nearest_points(l))
    print_ans(nearest_points(r))
    print_ans(nearest_points(p))

if __name__ == "__main__":
    main()
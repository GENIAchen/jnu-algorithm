import sys
import heapq

n = 0  # 顶点个数
g = [[0] * 11 for _ in range(11)]  # 邻接矩阵
best_cost = sys.maxsize
best_path = []

class Node:
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost
    def print_path(self):
        path_str = '->'.join(map(str, self.path))
        print(path_str)

# ls[i] < ls[2i+1] ; ls[i] < ls[2i+2]
# 用于将 open 数组调整为一个小根堆
# def EXTRACT_MIN(ls):
    # heapq.heapify(ls)

'''
    ls_length = len(ls)
    for i in range(1, ls_length):
        index = i
        while index > 0:
            if ls[index].cost < ls[(index - 1) // 2].cost:
                tmp = ls[index]
                ls[index] = ls[(index - 1) // 2]
                ls[(index - 1) // 2] = tmp
                index = (index - 1) // 2
            else:
                break
'''

def TSP_QUEUE():
    global best_cost, best_path
    open = []  # 优先队列
    open.append(Node([0], 0))
    count = 0
    while not len(open) == 0:
        count += 1
        print(f"count: {count}")
        open.sort(key=lambda node:node.cost)
        #print('open: ')
        #for i in range(len(open)):
        #   print(f"{open[i].cost}:{open[i].path}",end=" ")
        #print()
        cur = open[0]
        del open[0]
        #print('cur.path')
        #print(cur.path)
        #print()
        # 当前结点已经走过的路径长度要小于已求得的最短路径
        if cur.cost > best_cost:
            continue
        # 如果 cur 是叶子节点，判断是否需要更新最优值
        if len(cur.path) == n:
            total_cost = g[0][cur.path[-1]] + cur.cost
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = cur.path
        # 如果 cur 不是叶子节点，将其所有子节点加入队列中
        else:
            for i in range(0, n):
                if i not in cur.path:
                    cur_cost = cur.cost + g[cur.path[-1]][i]
                    new_path = cur.path[:]
                    new_path.append(i)
                    if cur_cost < best_cost:
                        open.append(Node(new_path, cur_cost))

def main():
    global best_cost, best_path, n, g
    n = eval(input())
    for i in range(0, n):
        row = list(map(int, input().split()))  # 只获取与顶点个数相匹配的数据
        for j in range(0, n):
            g[i][j] = row[j]
            if g[i][j] == 0:
                g[i][j] = sys.maxsize
    TSP_QUEUE()
    print(int(best_cost), end=": ")
    for i in range(n):
        best_path[i] += 1
    print('->'.join(map(str, best_path)))


if __name__ == "__main__":
    main()


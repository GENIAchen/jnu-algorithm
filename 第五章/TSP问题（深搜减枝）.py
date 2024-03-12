import queue
import sys

INF = sys.maxsize
n = 0  # 顶点个数
g = [[0] * 1005 for _ in range(1005)]  # 邻接矩阵
bestcost = INF  # 记录最优值
bestpath = []  # 记录最优路径

class Node:
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost
    
    def print_path(self):
        path_str = '->'.join(map(str, self.path))
        print(path_str)

def TSP_DFS():
    global bestcost, bestpath
    time = 0
    open_stack = queue.LifoQueue()  # 栈
    open_stack.put(Node([1], 0))  # 起始节点入栈
    while not open_stack.empty():
        cur = open_stack.get()
        time += 1
        if time <= 20:
            cur.print_path()  # 打印当前路径
        if cur.cost >= bestcost:
            continue
        if len(cur.path) == n:  # cur为叶子节点
            tot_cost = cur.cost + g[1][cur.path[-1]]
            if tot_cost < bestcost:  # 检测是否是更优解，更新最优解
                bestcost = tot_cost
                bestpath = cur.path
        else:  # cur不是叶子节点
            for i in range(n, 0, -1):  # 倒序生成所有满足条件的子节点并入栈
                if i not in cur.path:
                    cur_cost = cur.cost + g[cur.path[-1]][i]
                    if cur_cost < bestcost:
                        new_path = cur.path[:]
                        new_path.append(i)
                        open_stack.put(Node(new_path, cur_cost))

def main():
    global bestcost, bestpath
    global n, g
    n = int(input().split()[0])  # 从输入的第一个数字获取顶点个数
    for i in range(1, n + 1):
        row = list(map(float, input().split()))[:n]  # 只获取与顶点个数相匹配的数据
        for j in range(1, n + 1):
            g[i][j] = row[j - 1]
            if g[i][j] == 0:
                g[i][j] = INF
    TSP_DFS()
    print(int(bestcost), end=": ")
    print('->'.join(map(str, bestpath)))
    
if __name__ == "__main__":
    main()

# 暴力搜索,题目限定了水壶数量为 3,且只需要求出步数

# 定义 open 表和 close 表
open = []
close = []

# 三个水壶各自的容量
V = [int(x) for x in input().split()]
# 三个水壶的初始水量
origin = [int(x) for x in input().split()]
# 目标水量
target = eval(input())


# 定义节点类
class Node:
    # 到达当前状态经过的步数
    Dn = 0
    # 节点状态
    state = []

    # 节点类的构造函数
    def __init__(self, st, D):
        self.state = st
        self.Dn = D


# 定义一个用来输出节点信息的函数
def display(cur_node):
    print(f"当前步数：{cur_node.Dn}")
    print(cur_node.state)


# 判断当前状态是否已经在open表或close表中
def is_in_list(alist, new_state):
    state_ls = []
    for i in alist:
        state_ls.append(i.state)
    if new_state in state_ls:
        return 1
    else:
        return 0


# 找到对应状态在open表中的节点对应的最小深度
def how_much_is(alist, new_state):
    state_ls = []
    for i in alist:
        state_ls.append(i.state)
    idx = state_ls.index(new_state)
    return idx, alist[idx].Dn


# 指定节点的排序权值，使用节点的 Dn 值作为排序依据
def delta(node):
    return node.Dn


open.append(Node(origin, 0))
while open:
    cur_node = open.pop(0)
    close.append(cur_node)
    # display(cur_node)
    cur_state = cur_node.state
    for i in range(3):
        if cur_state[i] == target:
            print(cur_node.Dn)
            exit(0)
    for i in range(3):
        for j in range(3):
            if i != j and cur_state[j] < V[j]:
                new_state = cur_state.copy()
                if V[j] - cur_state[j] >= cur_state[i]:
                    new_state[j] += cur_state[i]
                    new_state[i] -= cur_state[i]
                elif V[j] - cur_state[j] < cur_state[i]:
                    new_state[j] = V[j]
                    new_state[i] = cur_state[i] - V[j] + cur_state[j]

                if is_in_list(close, new_state) != 1:
                    if is_in_list(open, new_state) != 1:
                        open.append(Node(new_state, cur_node.Dn + 1))
                    else:
                        index, smallest = how_much_is(open, new_state)
                        if cur_node.Dn + 1 < smallest:
                            open.pop(index)
                            open.append(Node(new_state, cur_node.Dn + 1))
    open.sort(key=delta)

print('None')








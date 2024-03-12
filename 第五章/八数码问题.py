import numpy as np

#定义open表，close表以及表示初始和目标状态的二维数组

open = []
close = []

start_state = np.zeros((3, 3), dtype=int)
target_state = np.zeros((3, 3), dtype=int)

#定义节点类
class Node:
    # 总代价(Fn = Dn + Wn)
    Fn = 0
    # 状态的深度，到达当前状态的步数
    Dn = 0
    # 不在位排数，作为启发信息的度量
    Wn = 0
    # 节点的状态
    state = np.zeros((3, 3), dtype=int)
    # 记录当前节点的父节点
    parent = []

    # 辅助函数：找到指定数字在状态中的位置
    def find_pos(self,state,num):
        for i in range(3):
            for j in range(3):
                if state[i][j] == num:
                    return i,j
                
    # 辅助函数：将空白格移动到指定位置(x,y)，生成新的状态
    def move_to(self,x,y):
        x0,y0 = self.find_pos(self.state,-1)
        new_state = self.state.copy()
        new_state[x0][y0] = new_state[x][y]
        new_state[x][y] = -1
        return new_state
    
    # 节点类的构造函数
    def __init__(self,state,prt=[]):
        self.state = state
        if prt:
            self.parent = prt
            self.Dn = prt.Dn + 1
        for i in range(3):
            for j in range(3):
                if state[i][j] != target_state[i][j]:
                    self.Wn += 1
        self.Fn = self.Dn + self.Wn


# 定义一个函数用于输出信息
def display(cur_node):
    print()
    print(f"总代价：{cur_node.Fn}")
    print(f"当前步数：{cur_node.Dn}")
    print('当前状态：')
    print(cur_node.state)

# 判断当前状态是否已经在close或者open表中
def is_in_list(alist,state):
    for i in range(len(alist)):
        if (alist[i].state == state).all():
            return i
    return -1

# 指定节点的排序权值，使用节点的 F 值作为排序依据
def delta(node):
    return node.Fn

r,c = map(int,input().split())
# 获取用户输入的初始状态
for i in range(3):
        start_state[i][0],start_state[i][1],start_state[i][2] = map(int,input().split())

# print('初始状态：')
# print(start_state)

# 填充目标状态
for i in range(3):
    for j in range(3):
        target_state[i][j] = 3*i + j
target_state[r][c] = -1

# print('目标状态')
# print(target_state)


# 将初始状态节点放入 open 表
open.append(Node(start_state))
while open:
    # 取出代价最小的节点进行扩展
    cur_node = open.pop(0)
    close.append(cur_node)
    # display(cur_node)
    # 判断是否为目标状态
    if (cur_node.state == target_state).all():
        # print('\nsuccess!')
        print(cur_node.Dn)
        exit(0)

    # 拓展节点，先找到 -1 的当前位置
    x,y = cur_node.find_pos(cur_node.state,-1)
    for [x_,y_] in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0 <= x_ < 3 and 0 <= y_ < 3:
            new = cur_node.move_to(x_,y_)
            # 判断新状态是否在close表
            if is_in_list(close,new) == -1:
                # 判断是否在 open 表中
                if is_in_list(open,new) == -1:
                    open.append(Node(new,cur_node))
                else:
                    # 更新总代价为较小值
                    index = is_in_list(open,new)
                    if cur_node.Dn + 1 < open[index].Dn:
                        open.pop(index)
                        open.append(Node(new,cur_node))
    # 按照Fn值进行排序
    open.sort(key = delta)
    # for i in open:
    #     print(i.Fn,end=" ")
    # print()






        





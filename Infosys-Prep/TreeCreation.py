from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.children = []
    def add_child(self,child):
        self.children.append(child)

a = Node("A")
b = Node("b")
c = Node("c")
d = Node("d")

a.add_child(b)
a.add_child(c)
b.add_child(d)

def dfs(node:Node):
    print(node.value)

    for child in node.children:
        dfs(child)



def bfs(root:Node):
    queue= deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        for child in node.children:
            queue.append(child)



class BTreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
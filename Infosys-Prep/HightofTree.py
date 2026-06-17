class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
def depth(self, root:Node):
    if root is None:
        return 0
    
    leftHight = self.depth(root.left)
    rightHight =self.depth(root.right)

    return 1+max(leftHight,rightHight)



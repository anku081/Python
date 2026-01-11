## General Tree Implementation in Python
'''class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def create_tree():
    data = input("enter node value: ")
    node = TreeNode(data)
    n = int(input("enter number of children for node {}: ".format(data)))
    for i in range(n):
        child = create_tree()
        node.children.append(child)
    return node


def print_tree(node, level=0):
    if node is not None:
        print(" " * level * 2 + str(node.value))
        for child in node.children:
            print_tree(child, level + 1)

t1 = create_tree()
print_tree(t1)'''

### Binary Tree Implementation in Python
'''class BinaryTreeNode:
    def __init(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def CreateBinaryTree():
    data =input("enter node value: ")
    if data == -1:
        return None
    node=BinaryTreeNode(data)
    print(f"Enter left child of {data}")
    node.left=CreateBinaryTree()
    print(f"Enter right child of {data}")
    node.right=CreateBinaryTree()
    return node

def printBinaryTree(node, level=0):
    if node is not None:
        print(" " * level * 2 + str(node.value))
        printBinaryTree(node.left, level + 1)
        printBinaryTree(node.right, level + 1)'''


'''class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def create_tree():
    data = input("enter node value: ")
    node = TreeNode(data)
    n = int(input("enter number of children for node {}: ".format(data)))
    for i in range(n):
        child = create_tree()
        node.children.append(child)
    return node

def print_tree(node, level=0):
    if node is not None:
        print(" " * level *2 + str(node.data))
        for child in node.children:
            print_tree(child, level+1)


t1 = create_tree()
print_tree(t1)'''

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def create_binary_tree():
    data = int(input("enter node value (-1 for no node): "))
    if data == -1:
        return None
    node = BinaryTreeNode(data)
    print(f"enter left child of {data}")
    node.left = create_binary_tree()
    print(f"enter right child of {data}")
    node.right = create_binary_tree()
    return node
def print_binary_tree(node, level=0):
    if node is not None:
        print(" " * level *2 + str(node.data))
        print_binary_tree(node.left, level+1)
        print_binary_tree(node.right, level+1)

'''def levelwise_traversal(root):
    if root is None:
        return 
    queue = []
    queue.append(root.data)
    while queue:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
        if  current.right:
            queue.append(current.right)'''

def maxLevelSum(root):
    if not root:
        return 0
    max_sum = float('-inf')
    level = float('-inf')
    queue = []
    queue.append(root)
    current_level = 0
    sum = []
    while queue:
        level_size = len(queue)
        current_level_sum = 0
        current_level += 1
        for _ in range(level_size):
            current = queue.pop(0)
            current_level_sum += current.data
            #print(f'{current_level} level sum: {current_level_sum}')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        sum.append(current_level_sum)
        #print(f'{current_level} level sum: {current_level_sum}')
        max_sum = max(max_sum, current_level_sum)
        if max_sum < current_level_sum:
            level = current_level
    for _ in range(len(sum)):
        if sum[_] == max_sum:
            level = _ + 1
            break
    return max_sum, level

'''def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node is not None:
        print(node.data, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=' ')'''


bt1 = create_binary_tree()
print_binary_tree(bt1)
print("Inorder Traversal:")
#inorder_traversal(bt1)  
#print("\nPreorder Traversal:")
#preorder_traversal(bt1)
#print("\nPostorder Traversal:")
#postorder_traversal(bt1)
#print("\nLevel-wise Traversal:")
#levelwise_traversal(bt1)
print("\nMaximum Level Sum:")
sum , level = maxLevelSum(bt1)
print(f"Maximum level sum is {sum} at level {level}")

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def CreateBinaryTree():
    data = int(input("Enter node value: "))
    if data == -1:
        return None
    node = BinaryTreeNode(data)
    print(f'Enter left child of : {data}')
    node.left = CreateBinaryTree()
    print(f'Enter right child of : {data}')
    node.right = CreateBinaryTree()
    return node

def printBinaryTree(node, level=0):
    if node is not None:
        print(" " * level * 2 + str(node.data))
        printBinaryTree(node.left, level+1)
        printBinaryTree(node.right, level+1)

def Inorder(node):
    if node:
        Inorder(node.left)
        print(node.data, end=" ")
        Inorder(node.right)

bt = CreateBinaryTree()
printBinaryTree(bt)
Inorder(bt)



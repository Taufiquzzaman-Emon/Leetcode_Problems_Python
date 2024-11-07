class Node:
    def __init__(self,v):
        self.data = v
        self.left = None
        self.right = None
def insert(node,value):
    if node is None:
        return node(value)
    if value<node.data:
        node.left = insert(node.left,value)
    else:
        node.right = insert(node.right,value)
    return node
def printPreorder(node):
    if node is None:
        return
    print(node.data,end = ' ')
    printPreorder(node.left)
    printPreorder(node.right)

preorder = [1,2,3,4,5,6]


def buildTree(preorder, index):
    if index >= len(preorder):
        return None, index

    # Create the root node with current value
    root = Node(preorder[index])
    index += 1
    
    # Construct left and right subtrees
    root.left, index = buildTree(preorder, index)
    root.right, index = buildTree(preorder, index)
    
    return root, index

# Build the tree from the preorder list
root, _ = buildTree(preorder, 0)

# Traverse the tree in preorder
print("Preorder Traversal of the constructed tree:")
printPreorder(root)

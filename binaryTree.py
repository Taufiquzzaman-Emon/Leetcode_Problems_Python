class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def build_binary_tree(preorder,index,n):
    if index[0]>=n:
        return None
    node = Node(preorder[index[0]])
    index[0]+=1

    if  index[0]<n:
        node.left=build_binary_tree(preorder,index,n)
        node.right = build_binary_tree(preorder,index,n)
    return node
def build_tree_from_preorder(preorder):
    index = [0]
    n = len(preorder)
    return build_binary_tree(preorder,index,n)
preorder = [7,5,4,6,3,1,2]
root = build_tree_from_preorder(preorder)
# if root.left.left and root.left.left.left:
#     print(root.left.left.left.data)
# print(root.right.data)

class BinaryTree:
    def __init__(self):
        self.tree = {}

    def add_node(self, root, left, right):
        self.tree[root] = (left, right)

    def preorder(self, node, result):
        if node == ".":
            return
        result.append(node)
        self.preorder(self.tree[node][0], result)
        self.preorder(self.tree[node][1], result)

    def inorder(self, node, result):
        if node == ".":
            return
        self.inorder(self.tree[node][0], result)
        result.append(node)
        self.inorder(self.tree[node][1], result)

    def postorder(self, node, result):
        if node == ".":
            return
        self.postorder(self.tree[node][0], result)
        self.postorder(self.tree[node][1], result)
        result.append(node)

import sys
data = sys.stdin.readlines()
n = int(data[0].strip())
binary_tree = BinaryTree()
for d in data[1:]:
    p, left, right = map(str, d.strip().split())
    binary_tree.add_node(p, left, right)

preorder_result = []
inorder_result = []
postorder_result = []
binary_tree.preorder("A", preorder_result)
binary_tree.inorder("A", inorder_result)
binary_tree.postorder("A", postorder_result)

print("".join(preorder_result))
print("".join(inorder_result))
print("".join(postorder_result))
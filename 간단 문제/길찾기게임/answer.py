import sys
sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.left = None
        self.right = None


def insert(root, child):
    if child.x < root.x:
        if root.left is None:
            root.left = child
        else:
            insert(root.left, child)
    else:
        if root.right is None:
            root.right = child
        else:
            insert(root.right, child)


def preorder(node, result):
    if node is not None:
        result.append(node.number)
        preorder(node.left, result)
        preorder(node.right, result)


def postorder(node, result):
    if node is not None:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.number)


def solution(nodeinfo):
    # 노드 생성 및 정렬 (y 내림차순, x 오름차순)
    nodes = []
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        nodes.append(Node(x, y, i + 1))

    nodes = sorted(nodes, key=lambda n: (-n.y, n.x))

    # 트리의 루트 노드
    root = nodes[0]

    # 트리 구성
    for node in nodes[1:]:
        insert(root, node)

    # 전위 순회와 후위 순회 결과 기록
    pre_result, post_result = [], []
    preorder(root, pre_result)
    postorder(root, post_result)

    return [pre_result, post_result]

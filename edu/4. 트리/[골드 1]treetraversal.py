# 메모리 초과
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def build_from_post_in(self, postorder, inorder):
#         """후위 순회와 중위 순회를 사용해 트리를 복원"""
#         def helper(postorder, inorder):
#             if not postorder or not inorder:
#                 return None
#
#             # 후위 순회에서 루트 값은 마지막 값
#             root_value = postorder[-1]
#             root = TreeNode(root_value)
#
#             # 중위 순회에서 루트의 위치를 찾음
#             root_index = inorder.index(root_value)
#
#             # 왼쪽과 오른쪽 서브트리 분리
#             left_inorder = inorder[:root_index]
#             right_inorder = inorder[root_index + 1:]
#             left_postorder = postorder[:len(left_inorder)]
#             right_postorder = postorder[len(left_inorder):-1]
#
#             # 재귀적으로 서브트리 생성
#             root.left = helper(left_postorder, left_inorder)
#             root.right = helper(right_postorder, right_inorder)
#
#             return root
#
#         self.root = helper(postorder, inorder)
#
#     def preorder_traversal(self, node=None, result=None):
#         """전위 순회: 루트 → 왼쪽 → 오른쪽"""
#         if result is None:
#             result = []
#         if node:
#             result.append(node.value)
#             self.preorder_traversal(node.left, result)
#             self.preorder_traversal(node.right, result)
#         return result
#
#     def inorder_traversal(self, node=None, result=None):
#         """중위 순회: 왼쪽 → 루트 → 오른쪽"""
#         if result is None:
#             result = []
#         if node:
#             self.inorder_traversal(node.left, result)
#             result.append(node.value)
#             self.inorder_traversal(node.right, result)
#         return result
#
#     def postorder_traversal(self, node=None, result=None):
#         """후위 순회: 왼쪽 → 오른쪽 → 루트"""
#         if result is None:
#             result = []
#         if node:
#             self.postorder_traversal(node.left, result)
#             self.postorder_traversal(node.right, result)
#             result.append(node.value)
#         return result
# import sys
# data = sys.stdin.readlines()
# inorder = list(map(int, data[1].strip().split()))
# postorder = list(map(int, data[2].strip().split()))
#
# tree = Tree()
# tree.build_from_post_in(postorder, inorder)
#
# # 결과 확인
# print(" ".join(str(t) for t in tree.preorder_traversal(tree.root)))
# #print("Pre-order Traversal (전위 순회):", " ".join(str(t) for t in tree.preorder_traversal(tree.root)))
# # print("In-order Traversal (중위 순회):", " ".join(str(t) for t in tree.inorder_traversal(tree.root)))
# # print("Post-order Traversal (후위 순회):", " ".join(str(t) for t in tree.postorder_traversal(tree.root)))

# 메모리 초과
# import sys
# sys.setrecursionlimit(10**6)
# data = sys.stdin.readlines()
# n = int(data[0])
# inorder = list(map(int, data[1].split()))
# postorder = list(map(int, data[2].split()))
#
# # 중위 순회의 값 → 인덱스 맵 생성
# inorder_map = {value: idx for idx, value in enumerate(inorder)}
# postorder_index = {idx: value for idx, value in enumerate(postorder)}
#
# def build_preorder(in_start, in_end, post_start, post_end):
#     if in_start > in_end or post_start > post_end:
#         return []
#
#     # 후위 순회의 마지막 값이 루트
#     root = postorder_index[post_end]
#
#     # 중위 순회에서 루트의 위치 찾기
#     root_index = inorder_map[root]
#
#     # 왼쪽 서브트리 크기 계산
#     left_size = root_index - in_start
#
#     # 왼쪽과 오른쪽 서브트리 처리
#     left = build_preorder(in_start, root_index - 1, post_start, post_start + left_size - 1)
#     right = build_preorder(root_index + 1, in_end, post_start + left_size, post_end - 1)
#
#     # 전위 순회: 루트 + 왼쪽 + 오른쪽
#     return [root] + left + right
#
#
# print(" ".join(map(str, build_preorder(0, n - 1, 0, n - 1))))

"""
아.. 개빡세네..
"""
import sys
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 중위 순회 값 → 인덱스 맵 생성
inorder_map = {value: idx for idx, value in enumerate(inorder)}

def build_preorder_iterative():
    stack = [(0, n - 1, 0, n - 1)]  # (in_start, in_end, post_start, post_end)
    preorder = []

    while stack:
        in_start, in_end, post_start, post_end = stack.pop()

        if in_start > in_end or post_start > post_end:
            continue

        # 후위 순회의 마지막 값이 루트
        root = postorder[post_end]
        preorder.append(root)

        # 중위 순회에서 루트의 위치 찾기
        root_index = inorder_map[root]

        # 왼쪽 서브트리 크기 계산
        left_size = root_index - in_start

        # 오른쪽 서브트리 추가 (스택에 먼저 추가)
        stack.append((root_index + 1, in_end, post_start + left_size, post_end - 1))

        # 왼쪽 서브트리 추가
        stack.append((in_start, root_index - 1, post_start, post_start + left_size - 1))

    return preorder

# 반복 방식으로 전위 순회 생성
print(" ".join(map(str, build_preorder_iterative())))






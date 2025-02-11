# import sys
# # data = sys.stdin.readlines()
# def preorder(data):
#     stack = []
#     postorder = []
#     root = []
#     for d in data:
#         if not stack:
#             stack.append(d)
#         else:
#             last_node = stack[-1]
#             insert_node = d
#             if insert_node < last_node:
#                 stack.append(insert_node)
#             else:
#                 if len(stack) < 2:
#                     stack_pop = stack.pop()
#                     if stack and stack[-1] < insert_node:
#                         postorder.append(stack_pop) #30
#                         root.append(stack.pop())
#                         stack.append(insert_node)
#                     else:
#                         if stack:
#                             root.append(stack.pop())
#                         root.append(stack_pop)
#                         stack.append(insert_node)
#                 while 2 < len(stack) and stack[-2] < insert_node:
#                     postorder.append(stack.pop())
#                 postorder.append(insert_node)
#     print(postorder)
#     print(stack)
#     print(root)
#     answer = postorder + stack[::-1] + root[::-1]
#     return answer
# # preorder([int(d) for d in data])
#
#
# print(" ".join(str(a) for a in preorder([8, 5, 1, 7, 10, 12])))
# print([1, 7, 5, 12, 10, 8])
# # preorder([10, 5, 2, 8, 15, 12, 20])
# # print([2, 8, 5, 12, 20, 15, 10])
# # preorder([50, 30, 20, 40, 70, 60, 80])
# # print([20, 40, 30, 60, 80, 70, 50])
# # preorder([5, 3, 2, 4, 7, 6, 8])
# # print([2, 4, 3, 6, 8, 7, 5])
# # preorder([1])
# # print([1])
# # preorder([1, 2, 3, 4, 5])
# # print([5, 4, 3, 2, 1])
# # preorder([5, 4, 3, 2, 1])
# # print([1, 2, 3, 4, 5])
# # preorder([30, 20, 10, 25, 40, 35, 50])
# # print([10, 25, 20, 35, 50, 40, 30])
# # preorder([10, 5, 3, 7, 15, 12, 20])
# # print([3, 7, 5, 12, 20, 15, 10])
# # preorder([15, 10, 5, 7, 12, 20, 17, 25])
# # print([7, 5, 12, 10, 17, 25, 20, 15])
# # preorder([50, 30, 20, 10, 25, 40, 35, 45, 70, 60, 55, 65, 80, 75, 85])
# # print([10, 25, 20, 35, 45, 40, 30, 55, 65, 60, 75, 85, 80, 70, 50])
# # preorder([100, 90, 80, 70, 60, 50])
# # print([50, 60, 70, 80, 90, 100])
# # preorder([1, 2, 3, 4, 5, 6])
# # print([6, 5, 4, 3, 2, 1])
# # preorder([10, 20, 15, 30, 25, 35])
# # print([15, 25, 35, 30, 20, 10])
# # preorder([500, 300, 200, 400, 700, 600, 800])
# # print([200, 400, 300, 600, 800, 700, 500])
# # preorder([50, 40, 30, 20, 10])
# # print([10, 20, 30, 40, 50])
# # preorder([10, 20, 30, 40, 50])
# # print([50, 40, 30, 20, 10])
# # preorder([5, 3, 4])
# # print([4, 3, 5])
# # preorder([100, 50, 25, 75, 150, 125, 175])
# # print([25, 75, 50, 125, 175, 150, 100])
# # preorder([40, 30, 20, 35, 50, 45])
# # print([20, 35, 30, 45, 50, 40])
# # preorder([20, 10, 25, 30, 35, 40])
# # print([10, 40, 35, 30, 25, 20])
# # preorder([15, 10, 8, 12, 20, 17, 25])
# # print([8, 12, 10, 17, 25, 20, 15])
# # preorder([15, 10, 8, 20, 17])
# # print([8, 10, 17, 20, 15])


import sys
sys.setrecursionlimit(10**6)
data = sys.stdin.readlines()
preorder = [int(d.strip()) for d in data]
answer_post_order = []
def post_order(start, end):
    if start > end:
        return

    index = start+1
    root = preorder[start]

    while index <= end and preorder[index] < root:
        index += 1

    post_order(start + 1, index-1)
    post_order(index, end)
    answer_post_order.append(root)

post_order(0, len(preorder) - 1)
print(" ".join(str(a) for a in answer_post_order))
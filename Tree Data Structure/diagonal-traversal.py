# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        queue = [A]
        ans = []
        while queue:
            node = queue.pop(0)
            while node:
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                node = node.right
        return ans

#https://www.interviewbit.com/problems/2sum-binary-tree/
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        if A is None:
            return 0
        hash_table = {}
        queue = [A]
        while queue:
            temp = queue.pop(0)
            if B-temp.val in hash_table:
                return 1
            hash_table[temp.val]=1
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return 0  

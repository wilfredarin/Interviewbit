
#symmetric-binary-tree
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isMirror(self,r1,r2):
        if r1 is None and r2 is None:
            return 1
        if r1 is not None and r2 is not None:
            if r1.val==r2.val:
                return self.isMirror(r1.left,r2.right) and self.isMirror(r1.right,r2.left)
        return 0
            
    def isSymmetric(self, A):
        if A is None:return 1
        return self.isMirror(A,A)

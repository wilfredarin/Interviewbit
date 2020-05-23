#https://www.interviewbit.com/problems/construct-binary-tree-from-inorder-and-preorder/
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        
        n = len(A)
        if n==0:
            return None
        root = TreeNode(A[0])
        ind = B.index(root.val)
        left = A[1:ind+1]
        right = A[ind+1:]
        root.left = self.buildTree(left,B[:ind])
        root.right = self.buildTree(right,B[ind+1:])
        return root
        

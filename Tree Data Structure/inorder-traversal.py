"""
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].

Using recursion is not allowed.
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        if not A:
            return None
        
        temp = A
        stack = []
        array = []
        while True:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                if stack:
                    temp = stack.pop()
                    array.append(temp.val)
                    temp = temp.right
                else:
                    
                    return array
        return array
            
                    
                
                
            
            

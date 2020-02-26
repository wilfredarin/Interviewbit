"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
min depth = 2.
"""
def minDepth(self, A):
        if A is None: return 0
        if not A.left and not A.right:
            return 1
        if not A.left:
            return self.minDepth(A.right)+1
        if not A.right:
            return self.minDepth(A.left)+1
        return min(self.minDepth(A.left),self.minDepth(A.right))+1

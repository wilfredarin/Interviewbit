#https://www.interviewbit.com/problems/largest-bst-subtree/
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        def largest(A):
            if A is None:
                return (True,0,200000,-20000000)
            if A.left is None and A.right is None:
                return(True,1,A.val,A.val)           
                #postorder
            l = largest(A.left)
            r = largest(A.right)
            
            is_bst = 0
            
            min_val = 0
            max_val = 0
            height = 0
        
            #root data > all in left( the max  of left<root) and root<right's min
            if l[0] and r[0] and l[3]<A.val and A.val<r[2]:
                min_val = min(A.val,l[2],r[2])
                max_val = max(A.val,l[3],r[3])
                is_bst = True
                height = l[1]+r[1] +1
                return ([is_bst,height,min_val,max_val])
            else:
                height = max(l[1],r[1])
                is_bst = False
                return ([is_bst,height,min_val,max_val])
        output = largest(A)
        return output[1]
            
            
        

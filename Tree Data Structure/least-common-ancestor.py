"""
Find the lowest common ancestor in an unordered binary tree given two values in the tree.

 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants. 
Example :


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor 
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.

"""
def lca(self, A, B, C):
	    if A is None:
	        return 
	    def findlca(A,B,C):
	        if A is None:
	            return
	        if A.val == B or A.val ==C:
	            return A.val
            left_lca = findlca(A.left,B,C)
            right_lca = findlca(A.right,B,C)
            if left_lca and right_lca:
                return A.val
            if left_lca:
                return left_lca
            else:
                return right_lca
	    def find(A,B):
	        if A is None:
	            return False
	        if A.val==B or find(A.left, B) or find(A.right,B):
	            return True
            return False
        
        if find(A,B) and find(A,C):
            return findlca(A,B,C)
        else:
            return -1
            

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        hash_table = {}
        queue = [(A,0)]
        while queue:
            a = queue.pop(0)
            x = a[1]
            a = a[0]
            if a :
                if a.left:
                    queue.append((a.left,x-1))
                if a.right:
                    queue.append((a.right,x+1))
                hash_table.setdefault(x,[]).append(a.val)
        ans =[]
        for i in sorted(hash_table.keys()):
            ans.append(hash_table[i])
        return ans

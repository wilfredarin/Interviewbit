#https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/
class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        def helpSum(A,ans):
            if A is None:
                return 0
            l = helpSum(A.left,ans)
            r  =helpSum(A.right,ans)
            max_single = max(l,r)+A.val
            ans = max(ans,max_single,A.val,l+r+A.val)
            return max_single
        ans = float("-inf")
        helpSum(A,ans)
        return ans

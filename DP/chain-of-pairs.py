#https://www.interviewbit.com/problems/chain-of-pairs/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if A[j][1]<A[i][0] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        return dp[-1]

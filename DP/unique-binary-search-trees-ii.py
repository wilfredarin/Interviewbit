#https://www.interviewbit.com/problems/unique-binary-search-trees-ii/
class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        n = A
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]

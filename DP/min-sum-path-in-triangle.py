class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        dp = A[-1]
        for i in range(n,0,-1):
            for j in range(1,i):
                dp[j-1] = min(dp[j-1],dp[j])+ A[i-2][j-1]
        return (dp[0])
        

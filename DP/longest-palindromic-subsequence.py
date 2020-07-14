https://www.interviewbit.com/problems/longest-palindromic-subsequence/
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for l in range(2,n+1):
            for i in range(n+1-l):
                if A[i] == A[i+l-1]:
                    dp[i][i+l-1] = 2 + dp[i+1][i+l-1-1]
                else:
                    dp[i][i+l-1] = max(dp[i][i+l-1-1],dp[i+1][i+l-1])
        return dp[0][n-1]
            
        

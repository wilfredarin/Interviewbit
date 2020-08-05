#https://www.interviewbit.com/problems/kth-manhattan-distance-neighbourhood/
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(B)
        m = len(B[0])
        dp = [[B[i][j] for j in range(m)] for i in range(n)]
        dp_1 = [[B[i][j] for j in range(m)] for i in range(n)]
        for k in range(A):
            for i in range(n):
                for j in range(m):
                    dp_1[i][j] = max(dp[i][j], dp[i-1][j] if i>0 else 0, dp[i+1][j] if i<n-1 else 0,
                    dp[i][j-1] if j>0 else 0,dp[i][j+1] if j<m-1 else 0)
            dp_1,dp = dp,dp_1
        return dp

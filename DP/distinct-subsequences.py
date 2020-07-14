#https://www.interviewbit.com/problems/distinct-subsequences/
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        m = len(A)
        n = len(B)
        dp = [[0 for i in range(m+1)] for j in  range(n+1)]
        for i in range(m+1):
            dp[0][i] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                soln1 = dp[i][j-1]
                soln2 = 0
                if A[j-1] == B[i-1]:
                    soln2 = dp[i-1][j-1]
                dp[i][j] = soln1+soln2
        return dp[-1][-1]
                

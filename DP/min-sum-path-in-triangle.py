class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
    
        dp = [0]*n
        # get the last row in dp
        for i in range(n):
            dp[i]=A[n-1][i]
        #now go from bot to up
        #only adjacent elements :
        #start with second last row now and go in reverse till the i=0
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = min(dp[j],dp[j+1])+A[i][j]
        return dp[0]

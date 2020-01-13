def minPathSum(self, A):
        n = len(A)
        m = len(A[0])
        dp = [[[0] for i in range(m)] for j in range(n)]#don't do dp = [[0]*m]*n as 
        dp[0][0] = A[0][0]                               #it creates copy of same row!!
        for j in range(1,m):
            dp[0][j] = dp[0][j-1]+A[0][j]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]+A[i][0]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+A[i][j]
        #print(dp)
        return dp[-1][-1]

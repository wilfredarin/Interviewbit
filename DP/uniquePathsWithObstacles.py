def uniquePathsWithObstacles(self, A):
        n = len(A)
        m = len(A[0])
        if not A[0][0]:
            dp = [[0 for i in range(m)] for j in range(n)]
            for i in range(n):
                if not A[i][0]:
                    dp[i][0] = 1
                if A[i][0]:
                    break
            for j in range(m):
                if not A[0][j]:
                    dp[0][j] = 1
                if A[0][j]:
                    break
            for i in range(1,n):
                for j in range(1,m):
                    if not A[i][j]:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[-1][-1]

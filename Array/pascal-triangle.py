def solve(self, A):
        n = A
        if n==0:
            return []
        elif n==1:
            return [[1]]
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        dp[0][1] = 1
        ans = []
        for i in range(1,n+1):
            l = []
            for j in range(1,i+1):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                l.append(dp[i][j])
            ans.append(l)
        return ans

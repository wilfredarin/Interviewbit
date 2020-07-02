#https://www.interviewbit.com/problems/longest-arithmetic-progression/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n<=2:
            return n
        A = sorted(list(A))
        dp = [[0 for i in range(n)] for j in range(n)]
        llap = 2 
        for i in range(n):
            dp[i][n-1] = 2
        for j in range(n-2,0,-1):
            l = j-1
            r = j+1
            while(l>=0 and r<=n-1):
                if (A[l] + A[r] < 2*A[j]):
                    r+=1
                elif (A[l] + A[r] > 2*A[j]):
                    dp[l][j] = 2
                    l-=1
                else:
                    dp[l][j] = dp[j][r]+1
                    llap = max(dp[l][j],llap)
                    l -=1
                    r +=1
                    while(l>=0):
                        dp[l][j] = 2
                        l-=1
        return llap
                    
        

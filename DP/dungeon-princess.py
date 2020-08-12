#https://www.interviewbit.com/problems/dungeon-princess/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        n = len(A)
        m = len(A[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        #set the base case
        if A[-1][-1]>0:
            dp[-1][-1] = 1
        else:
            dp[-1][-1] = abs(A[-1][-1])+1 
        
        #set the last col
        for i in range(n-2,-1,-1):
            dp[i][m-1] = max(dp[i+1][m-1]-A[i][m-1],1)
        #set last row
        for i in range(m-2,-1,-1):
            dp[n-1][i] = max(dp[n-1][i+1]-A[n-1][i],1)
        #fil bot up
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                min_to_leave  = min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = max(min_to_leave-A[i][j],1)
        return dp[0][0]
            
            
        

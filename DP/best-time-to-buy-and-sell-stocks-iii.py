#https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-iii/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A)<2:
            return 0
        dp = [[0 for j in range(len(A))] for i in range(3)]
        for i in range(1,3):
            maxdiff = float("-inf")
            for j in range(1,len(A)):
                maxdiff = max(dp[i-1][j-1]-A[j-1],maxdiff) 
                dp[i][j] = max(dp[i][j-1],maxdiff+A[j])
        return dp[-1][-1]
                
            

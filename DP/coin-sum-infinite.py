#https://www.interviewbit.com/problems/coin-sum-infinite/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        dp = [0  for i in range(B+1)]
        dp[0] = 1
        for coin in A:
            for i in range(coin,B+1):
                dp[i]+=dp[i-coin]
        return dp[-1]%(10**6+7)
        

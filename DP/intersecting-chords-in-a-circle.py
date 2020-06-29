#https://www.interviewbit.com/problems/intersecting-chords-in-a-circle/
class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        n = 2*A
        
        dp = [0 for i in range(n+1)]
        
        dp[0] = 1
        dp[2] = 1
        for i in range(4,n+1,2):
            for j in range(0,i-1,2):
                dp[i]+=(dp[j]*dp[i-2-j])%(10**9+7)
        return dp[n]%(10**9+7)

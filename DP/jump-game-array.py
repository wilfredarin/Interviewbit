#https://www.interviewbit.com/problems/jump-game-array/
class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        n = len(A)
        if not A:
            return 0
        if A[0]==1 and n!=1:
            return 0
        dp = [0 for i in range(n)]
        dp[0] = 1 
        max_jump = A[0]
        for i in range(n):
            if A[i] and dp[i]:
                max_jump = A[i]
                for j in range(1,max_jump+1):
                    if j+i<n:
                        dp[i+j]=1
                    else:
                        break
        
        return dp[-1]    

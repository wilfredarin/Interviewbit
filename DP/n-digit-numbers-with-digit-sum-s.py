#https://www.interviewbit.com/problems/n-digit-numbers-with-digit-sum-s-/
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dp = [[0]*(B+1) for i in range(A+1)]
        modulo = 1000000007
        #digit our col 
        #sum our rows
        dp[0][0] = 1
        flag = False
        for i in range(1,A+1):
            for j in range(1,B+1):
                for k in range(10):
                    #check leading Zero
                    if not flag:
                        flag = True
                        continue
                    if j-k>=0:
                        dp[i][j]+=dp[i-1][j-k]
        return dp[-1][-1]%modulo
                    
    
       

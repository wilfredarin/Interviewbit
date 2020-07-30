#https://www.interviewbit.com/problems/regular-expression-match/
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        
        s_l = len(A)
        p_l = len(B)
        pattern = [B[0]]
        pr = B[0]
        for i in range(1,p_l):
            if not (pr=="*" and B[i]=="*"):
                pattern.append(B[i])
                pr = B[i]
        p_l = len(pattern)
                
                
        dp = [[False for i in range(p_l+1)] for j in range(s_l+1)]
        dp[0][0] = True
        
        for j in range(1,p_l+1):
            if pattern[j-1]=="*":
                dp[0][j] = dp[0][j-1]
        
        for i in range(1,s_l+1):
            for j in range(1,p_l+1):
                if pattern[j-1]=="*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif pattern[j-1]=="?" or pattern[j-1]==A[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        
        if dp[-1][-1]:
            return 1
        else:
            return 0
        
                    

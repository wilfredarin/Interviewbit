#https://www.interviewbit.com/problems/min-jumps-array/
class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n==0 :
            return -1
        if n>1 and A[0]==0:
            return -1
        if n==1:
            return 0
        steps = A[0]
        maxReach = A[0]
        jumps = 1
        for i in range(1,n):
            steps-=1
            if i==n-1:
                return jumps
            maxReach = max(maxReach,i+A[i])
            if steps==0:
                jumps+=1
                if i>=maxReach:
                    return -1
                steps = maxReach-i
        return -1
                
            
            
        
                
                    
            

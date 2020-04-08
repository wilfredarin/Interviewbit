#https://www.interviewbit.com/problems/tushars-birthday-party/

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        max_c = max(A)
        min_c = min(B)
        ans = 0
        costs = [0 for i in range(max_c+1)]
        for i in range(min_c,max_c+1):
            costs[i] = min([costs[i-taken] + C[index] for index,taken in enumerate(B) if taken<=i])
        for i in A:
            ans+=costs[i]
        return ans    
        
        

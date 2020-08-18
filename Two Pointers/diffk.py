#https://www.interviewbit.com/problems/diffk/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        if n<2:
            return 0
        i = 0
        j = 1
        for i in range(n-1):
            j = max(j,i+1)
            while j<n-1 and A[j]-A[i]<B:
                j+=1
            if A[j]-A[i]==B:
                return 1
        return 0
        

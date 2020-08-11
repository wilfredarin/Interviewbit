#https://www.interviewbit.com/problems/max-product-subarray/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        n = len(A)
        max_here = 1
        min_here = 1
        max_all = -float("inf")
        for i in range(n):
            if A[i]>0:
                max_here *=A[i]
                min_here = min(min_here*A[i],1)
            elif A[i]==0:
                max_here = 0
                min_here = 1 
            else:
                temp = max_here
                max_here = min_here*A[i]
                min_here = temp*A[i]
            max_all = max(max_here,max_all)
            if max_here<=0:
                max_here = 1
        return max_all
                

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        """s = sum(A)
        t = sum(set(A))
        return abs(s-2*t)"""
        A = list(A)
        for i in range(len(A)-1):
            A[i+1] = A[i]^A[i+1]
        return A[-1]
"""
from functools import reduce
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):

        return reduce(lambda x,y : x^y, A)
"""
            
            
    
                
        

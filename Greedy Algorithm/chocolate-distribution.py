#https://www.interviewbit.com/problems/chocolate-distribution/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
 
    # make sure 0+B-> 0+4=4 : 0,1,2,3,4 (5 values) ;;;B-1
    def solve(self, A, B):
        if not A or B==0:
            return 0
        A.sort()
        m = float('inf')
        for i in range(len(A)-B+1):
            if A[i+B-1]-A[i]<=m:
                m = A[i+B-1]-A[i]
        return m

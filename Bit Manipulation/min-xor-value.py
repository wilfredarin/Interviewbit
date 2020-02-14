class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        m = 99999999999
        for i in range(len(A)-1):
            j = i+1
            m = min(A[i]^A[j],m)
        return m

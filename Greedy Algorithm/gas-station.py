#https://www.interviewbit.com/problems/gas-station/
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        fuel = 0
        start = 0
        sum = 0
        n  = len(A)
        for i in range(n):
            sum+=A[i]-B[i]
            fuel+=A[i]-B[i]
            if fuel<0:
                fuel = 0
                start=i+1
        if sum>=0:
            return start%n
        else:
            return -1

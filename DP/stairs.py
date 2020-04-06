#https://www.interviewbit.com/problems/stairs/
class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        n =  A
        if A <3:
            return A
        stairs = [0 for i in range(n+1)]
        stairs[1]=1
        stairs[2] = 2
        for i in range(3,n+1):
            stairs[i]=stairs[i-1]+stairs[i-2]
        return stairs[n]

#https://www.interviewbit.com/problems/ways-to-color-a-3xn-board/
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        color2 =  12
        color3 = 24
        for i in range(2,A+1):
            temp = color2
            color2 = color3*5 +color2*7
            color3 = temp*10 + color3*11
        return (color2+color3)%(10**9+7)
    

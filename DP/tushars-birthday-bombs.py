#https://www.interviewbit.com/problems/tushars-birthday-bombs/
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        weakest_frnd = float("inf")
        F = 0
        
        for i in range(len(B)):
            if B[i]<weakest_frnd:
                weakest_frnd = B[i]
                F = i
        
        num_kicks = A//B[F]
        extra_possible = A%B[F]
        ans = [F]*num_kicks
        i= 0
        j = 0
        
        while j<F and i<num_kicks:
            if B[j] - weakest_frnd<=extra_possible:
                extra_possible-=B[j] - weakest_frnd
                ans[i] = j
                i+=1
            else:
                j+=1
        return ans
                
        
        

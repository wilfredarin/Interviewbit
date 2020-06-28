#https://www.interviewbit.com/problems/find-permutation/
class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        left = [i for i in range(1,B+1)]
    
        ans = []
        for i in A:
        
            if i=="D":
                ans+=[left.pop()]
            else:
                ans+=[left.pop(0)]
                
        return ans+[left.pop()]
            
            
        

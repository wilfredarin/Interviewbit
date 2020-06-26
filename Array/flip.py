#https://www.interviewbit.com/problems/flip/
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        cur = 0
        max_diff = 0
        l = 0
        r = 0
        n = len(A)
        ans = []
        for i in range(n):
            r = i
            if A[i]=="0":
                cur = max(1,cur+1)
            else:
                cur = max(-1,cur-1)
            
            if cur>max_diff:
                ans = [l+1,r+1]
                max_diff = cur
            # elif cur==max_diff:
            #     ans.append([l+1,r+1])
            if cur<=-1:
                l=i+1
        return ans    
                
                
                

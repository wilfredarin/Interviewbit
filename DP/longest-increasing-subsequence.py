#https://www.interviewbit.com/courses/programming/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n = len(A)
        if not A:
            return 0
        ans = [1 for i in range(n)]
        dp = 0
        for i in range(1,n):
            for j in range(i):
                if A[i]>A[j]:
                    ans[i]=max(ans[i],ans[j]+1)
        return max(ans)            
                

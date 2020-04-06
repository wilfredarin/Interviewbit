#https://www.interviewbit.com/problems/length-of-longest-subsequence/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n = len(A)
        if not A:
            return 0
        lis = [1 for i in range(n)]
        lds = [1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if A[j]<A[i]:
                    lis[i]=max(lis[i],lis[j]+1)
        for i in range(n-2,-1,-1):
            for j in range(n-1,i,-1):
                if A[j]<A[i]:
                    lds[i]=max(lds[i],lds[j]+1)
        ans = lis[0] + lds[0] - 1
        for i in range(1,n):
            ans = max(ans,lds[i]+lis[i]-1)
        return ans
         

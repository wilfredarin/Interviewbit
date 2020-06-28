#https://www.interviewbit.com/problems/next-permutation/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        n = len(A)
        for i in range(n-2,-1,-1):
            prev = A[i+1]
            now = A[i]
            if prev>now:
                k = i+1
                while k<n and now<A[k]:
                    k+=1
                k-=1
                A[i],A[k] = A[k],A[i]
                r = n-1
                l = i+1
                while l<r:
                    A[l],A[r] = A[r],A[l]
                    l+=1
                    r-=1
                return A
        A.sort()
        return A
        
            
            

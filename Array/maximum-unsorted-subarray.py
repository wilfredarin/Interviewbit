#https://www.interviewbit.com/problems/maximum-unsorted-subarray/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        s = -1
        cur = A[0]
        for i in range(1,n):
            Next = A[i]
            if cur>Next:
                s = i-1
                break
            cur = A[i]
        cur = A[-1]
        e = -1
        for i in range(n-2,-1,-1):
            Next = A[i]
            if Next>cur:
                e=i+1
                break
            cur = A[i]
        
        if s ==-1 and e==-1:
            return [-1]
        else:
            mi = min(A[s:e+1])
            ma = max(A[s:e+1])
            for i in range(s):
                if A[i]>mi:
                    s = i
                    break
            for i in range(n-1,e,-1):
                if A[i]<ma:
                    e = i
                    break
        return [s,e]
                    
                
                
                
            

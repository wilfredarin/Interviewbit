#https://www.interviewbit.com/problems/word-break/
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        if B is None:
            return 0
        if A is None:
            return 1
        n = len(A)
        store = {}
        for i in range(n-1,-1,-1):
            #from last element
            for j in range(i+1,n+1):
                #from i+1 to (last+1)th element 
                if A[i:j] in B:#corner case last element
                    if j<n:#if j not the last element(to avoid out of bound in A[j:])
                        if A[i:j] in B and A[j:] in store:
                            store[A[i:]]=1
                            break
                    elif j==n:
                        store[A[i:]]=1
        if A in store:
            return 1
        else:
            return 0
        
    
                    

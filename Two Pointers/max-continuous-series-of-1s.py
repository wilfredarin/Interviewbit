class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        """
        def removeElement(self, A, B):
        A[:] = [ii for ii in A if ii != B]
        return len(A)
        """
        cur = 0
        t =0 
        for i in range(len(A)):
            if A[i]!=B:
                A[cur]=A[i]
                cur+=1
            else:
                t+=1
        A =A[:len(A)-t]
        return len(A)
        

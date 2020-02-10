class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        n = len(A)
        m = len(A[0])
        k = []
        for i in A:
            k+=i
        l = 0
        h = m*n-1
        while l<=h:
            mid = (l+h)//2
            if k[mid]==B:
                return 1
            if B<k[mid]:
                h = mid -1
            else:
                l = mid+1
        return 0 

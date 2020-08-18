#https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        fp = 2
        cp = 2
        while fp<n:
            if A[cp-2]!=A[fp]:
                A[cp] = A[fp]
                cp+=1 
            fp+=1 
        return cp
                
                
                
            
            
            
                
            

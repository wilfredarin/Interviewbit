#https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        n = len(A[0])
        grid = A
	    incl = max(grid[0][0], grid[1][0]) 
	    excl = 0
	    for i in range(1, n) : 
		    excl_new = max(excl, incl)
		    incl = excl + max(grid[0][i], grid[1][i]) 
		    excl = excl_new 
	    return max(excl, incl)
    

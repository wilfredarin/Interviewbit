#https://www.interviewbit.com/problems/largest-area-of-rectangle-with-permutations/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A: return 0 
        n = len(A)
        
        
        m = len(A[0])
        #print(m)
        histogram = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i==0:
                    histogram[i][j] = A[i][j]
                else:
                    if A[i][j]==1:
                        histogram[i][j] = histogram[i-1][j]+1
                    else:
                        histogram[i][j] = 0
        
        #print(histogram)
        for i in range(n):
            histogram[i] = sorted(histogram[i],reverse=True)
        
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                max_area = max(max_area,histogram[i][j]*(j+1))
        return max_area
                        
            

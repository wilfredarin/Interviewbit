#https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def histogramArea(self,row):
        n = len(row)
        max_area = 0
        stack = []
        i = 0
        while i<n:
            if not stack or row[stack[-1]]<=row[i] :
                stack.append(i)
                i+=1
            else:
                while stack and row[stack[-1]]>row[i]:
                    index = stack.pop()
                    if stack:
                        max_area = max(max_area,(i-stack[-1]-1)*row[index])
                    else:
                        max_area = max(max_area,i*row[index]) 
        while stack:
            index = stack.pop()
            if stack:
                max_area = max(max_area,(i-stack[-1]-1)*row[index])
            else:
                max_area = max(max_area,i*row[index])
        return max_area
                
                
    def maximalRectangle(self, A):
        n = len(A) 
        m = len(A[0])
        histogram = [0 for i in range(m)]
        area = 0
        for i in range(n):
            row = A[i]
            for j in range(m):
                if row[j]:
                    histogram[j]+=1
                else:
                    histogram[j]=0
            area = max(area,self.histogramArea(histogram))
        return area
        
        

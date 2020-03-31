"""
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of 
the ith histogram’s bar. Width of each bar is 1.

Largest Rectangle in Histogram: Example 1

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Largest Rectangle in Histogram: Example 2

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Find the area of largest rectangle in the histogram.



Input Format

The only argument given is the integer array A.
Output Format

Return the area of largest rectangle in the histogram.
For Example

Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
    Explanation 1:
        The largest rectangle is shown in the shaded area, which has area = 10 unit.
"""

class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
	    n = len(A)
	    stack = []
	    area = -1
	    i = 0
	    while i<n:
	        if not stack or A[stack[-1]]<=A[i]:
	            stack.append(i)
	            i+=1
            else:
                while stack and A[stack[-1]]>A[i]:
                    index = stack.pop()
                    if stack:
                        area = max(area,A[index]*(i-stack[-1]-1))
                    else:
                        area = max(area,A[index]*i)
        while stack:
            index = stack.pop()
            if stack:
                area = max(area,A[index]*(i-stack[-1]-1))
            else:
                area = max(area,A[index]*i)
        return area
            

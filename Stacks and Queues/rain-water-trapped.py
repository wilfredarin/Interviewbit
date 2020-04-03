"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Input Format

The only argument given is integer array A.
Output Format

Return the total water it is able to trap after raining..
For Example

Input 1:
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
Output 1:
    6
Explaination 1: <img src="http://i.imgur.com/0qkUFco.png">
    
    In this case, 6 units of rain water (blue section) are being trapped.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        left = []
        maximum = -1
        for i in range(n):
            if A[i]>maximum:
                left.append(A[i])
                maximum = A[i]
            else:
                left.append(maximum)
        right = []
        maximum = -1
        for i in range(n-1,-1,-1):
            if A[i]>maximum:
                right.append(A[i])
                maximum = A[i]
            else:
                right.append(maximum)
        right.reverse()
        ans = 0
        for i in range(n):
            m = min(left[i],right[i])
            if m >A[i]:
                ans+=m-A[i]
        return ans        

#method 2 Stack  Interviewbit
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        # Visits each element of the array A twice
        # (stacking and popping).
        # If the stack is implemented in a more basic
        # form and stack[0] is not a fast operation,
        # we could store the current maximal element
        # separately.
        stack = []
        water = 0
        for a in A:
            if stack and stack[0]<=a:
                h = stack[0]
                while stack:
                    water += h-stack.pop()
            stack.append(a)
        h = stack.pop()
        while stack:
            n = stack.pop()
            if n > h:
                h = n
                continue
            water += h-n
        return water

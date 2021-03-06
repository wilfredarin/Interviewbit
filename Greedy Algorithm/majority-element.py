"""
Programming Greedy Algorithm Majority Element
Majority Element
Asked in:  
Microsoft
Yahoo
Google
Amazon
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :


Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2. 
"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def majorityElement(self, A):
	    n = len(A)
	    counter =  1
	    prev = A[0]
	    for i in range(1,n):
	        if prev == A[i]:
	            counter+=1
            else:
                counter-=1
            if counter == 0:
                prev = A[i]
                counter = 1
        return prev

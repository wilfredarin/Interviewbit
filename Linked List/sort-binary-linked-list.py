#https://github.com/wilfredarin/Interviewbit/new/master/Linked%20List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        count_0 = 0
        count_1 = 0
        temp  = A 
        while temp:
            if temp.val:
                count_1+=1
            else:
                count_0+=1 
            temp = temp.next 
        temp = A
        while count_0:
            temp.val = 0
            temp = temp.next 
            count_0-=1
        while count_1:
            temp.val = 1
            temp = temp.next
            count_1-=1
        return A
            
            
            
            
            
            
            

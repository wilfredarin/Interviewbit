# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        prev = None 
        temp = A
        while temp:
            if prev and prev.val == temp.val:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return A

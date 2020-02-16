# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        cur_a = A
        cur_b = B
        C=cur = ListNode(None)
        while cur_a and cur_b:
            if cur_a.val<cur_b.val:
                cur.next = cur_a
                cur_a = cur_a.next
            else:
                cur.next = cur_b
                cur_b = cur_b.next
            cur = cur.next
        if cur_a:
            cur.next = cur_a
        if cur_b:
            cur.next = cur_b
        return C.next
        
            
                

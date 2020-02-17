# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        temp = A
        head1 =ListNode(0)
        head2 = ListNode(0)
        right,left = head2,head1
        while temp:
            if temp.val<B:
                left.next = temp
                left = temp
            else:
                right.next = temp
                right = temp
            temp = temp.next
        left.next = head2.next
        right.next = None
        return head1.next
            
        
            
            

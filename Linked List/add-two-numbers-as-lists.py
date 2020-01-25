# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        temp = A
        t = 0
        while temp:
            temp = temp.next
            t+=1
        temp = B
        d = 0
        while temp:
            temp = temp.next
            d+=1
        carry = 0
        if t>d:
            s = 0
            temp1= A
            temp2 = B
            prev = None
        else:
            temp1 = B
            temp2 = A
            prev = None
        c = 0
        while temp2:
            s = 0
            s+=temp1.val+temp2.val +c
            c=s//10
            s = s%10
            temp1.val  = s
            prev = temp1
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1:
            s = c+temp1.val
            c = s//10
            s = s%10
            prev = temp1
            temp1.val = s
            temp1  = temp1.next
        if c:
            prev.next = ListNode(c)
                
        if t>d:
            return A
        else:
            return B
                
                
            
        
            
            
            
            
                        
            
            
            

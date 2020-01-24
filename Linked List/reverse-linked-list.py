def reverseList(self, A):
        temp = A
        Next = None
        prev  = None 
        while temp:
            Next = temp.next
            temp.next = prev
            prev = temp
            temp = Next
            
        A.head = prev
        return A.head

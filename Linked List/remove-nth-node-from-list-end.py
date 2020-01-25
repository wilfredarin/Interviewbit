 def removeNthFromEnd(self, A, B):
        temp = A
        c = 0
        prev = None
        Next = None
        while temp:
            temp = temp.next
            c+=1
        if c==1:
            return None
        if c<=B :
            temp = A
            Next = temp.next
            temp = None
            return Next
        n = c-B -1
        c = 0
        temp = A
        while c!=n:
            temp = temp.next
            c+=1
        a = temp.next
        temp.next = temp.next.next
        a = None
        return A

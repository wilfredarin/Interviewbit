def rotateRight(self, A, B):
        temp = A
        c = 0
        while temp:
            c+=1
            temp = temp.next
        B = B%c
        if B==0:
            return A
        c = c - B
        temp = A
        for i in range(c-1):
            temp = temp.next
        b = temp.next
        temp.next = None
        temp = b 
        while temp.next:
            temp = temp.next
        temp.next = A
        return b

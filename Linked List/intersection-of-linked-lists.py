def getIntersectionNode(self, A, B):
        temp = A
        c = 0
        while temp:
            temp = temp.next
            c+=1
        temp2  = B
        d = 0
        
        while temp2:
            temp2 = temp2.next
            d+=1
        temp = A
        temp2 = B
        if c>d:
            t = 0
            while t<c-d:
                temp = temp.next
                t+=1
        else:
            t = 0
            while t<d-c:
                temp2 = temp2.next
                t+=1
        while temp and temp2:
            if temp ==temp2:
                return temp
            temp = temp.next
            temp2 = temp2.next
        return None

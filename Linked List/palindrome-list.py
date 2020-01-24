def lPalin(self, A):
        a = []
        temp = A
        c = 0
        while temp:
            a.append(temp.val)
            c+=1
            temp = temp.next
        if c%2 == 0:
            t = a[:c//2]
            b = a[c//2:]
            b = b[::-1]
            
        else:
            t = a[:c//2]
            b = a[c//2+1:]
            b = b[::-1]
        if t==b:
            return 1
        else:
            return 0

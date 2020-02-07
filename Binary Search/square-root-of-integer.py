def sqrt(self, A):
        l = 0
        h = A//2
        val =0
        if A==0:
            return A
        if A==1 or A==2 or A==3:
            return 1
        while l<=h:
            m = l+(h-l)//2
            t  = m*m
            if t==A:
                return m
            if t>A:
                h = m-1
            else:
                l = m+1
                val = m
        return val

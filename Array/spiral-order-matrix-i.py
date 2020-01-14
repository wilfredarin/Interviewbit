def spiralOrder(self, A):
        n = len(A)
        m = len(A[0])
        r = 0
        c = 0
        b = []
        while r<n and c<m:
            for i in range(c,m):
                b.append(A[r][i])
            r+=1 
            for j in range(r,n):
                b.append(A[j][m-1])
            m -=1 
            
            if r<n:
                for i in range(m-1,c-1,-1):
                    b.append(A[n-1][i])
                n-=1 
            if c<m:
                for j in range(n-1,r-1,-1):
                    b.append(A[j][c])
                c+=1 
        return (b)

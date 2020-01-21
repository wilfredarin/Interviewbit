def setZeroes(self, A):
        n = len(A)
        m = len(A[0])
        r = [1]*n
        c = [1]*m
        for i in range(n):
            for j in range(m):
                if A[i][j]==0:
                    c[j]=0
                    r[i]=0
        for i in range(n):
            if r[i]==0:
                A[i] = [0]*m
            else:
                A[i] = [A[i][j]*c[j] for j in range(m)] 
        return A

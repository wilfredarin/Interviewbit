def maxArr(self, A):
        n = len(A)
        b = []
        c = []
        for i in range(n):
            b.append(A[i]+i)
            c.append(A[i]-i)
        b.sort()
        c.sort()
        a = max(abs(b[-1]-b[0]),abs(c[-1]-c[0]))
        return a

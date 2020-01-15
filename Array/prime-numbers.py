def sieve(self, A):
        b = []
        a = [0 for i in range(A+1)]
        for i in range(2,A):
            if not a[i]:
                b.append(i)
                for j in range(i,A,i):
                    a[j] = 1
        return(b)

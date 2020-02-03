def repeatedNumber(self, A):
        n = len(A)
        a = [0]*(n+1)
        for i in A:
            if not a[i]:
                a[i]=1
            else:
                return i

def findRank(self, A):
        a = list(A)
        a.sort()
        n = len(a)
        b  =list(A)
        k =math.factorial(n-1)
        ans= 0
        d = n
        while b:
            t = b.pop(0)
            i  = a.index(t)
            a.remove(t)
            ans+=i*(k)
            if d>1:
                d-=1
                k //=d
            else:
                k=1
        ans = ans+1
        return ans%1000003

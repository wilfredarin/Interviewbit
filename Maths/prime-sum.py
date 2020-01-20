def prime_list(self,n):
        l = [0]*(n+1)
        l[0] = 1
        l[1] = 1
        ans = []
        s = int(n**(.5))
        for i in range(2,s+1):
            if l[i]==0:
                for j in range(i+i,n+1,i):
                    l[j]=1
                ans.append(i)
        for j in range(s+1,n+1):
            if l[j]==0:
                ans.append(j)
        for i in ans:
            if l[n-i]==0:
                return [i,n-i]
    def primesum(self, A):
        return self.prime_list(A)

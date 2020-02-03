def firstMissingPositive(self, A):
        n = 0
        ans = [0]*(len(A)+1)
        for i in A:
            if i>0 and i<n+1:
                ans[i]=1

        for i in range(1,n+1):
            if ans[i]==0:
                return i
                
        return n+1

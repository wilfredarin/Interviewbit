import bisect
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def divProd(self,x):
        ans =1
        m = 1000000007
        for i in range(1,int(x**.5)+1):
            if x%i==0:
                if x/i!=i:
                    ans=(ans*(x/i))%(m)
                    ans=(ans*i)%(m)
                else:
                    ans=(ans*i)%m
        return int(ans%(m))
    def freq(self,A):
        n = len(A)
        L = [1]*n
        s = []
        top =-1
        for i in range(n):
            while top>=0 and A[s[top]]<=A[i]:
                s.pop()
                top-=1
            if top>=0:
                L[i] = i-s[top]
            else:
                L[i] = i+1
            s.append(i)
            top+=1
        s = []
        top = -1
        R = [1]*n
        for i in range(n-1,-1,-1):
            while top>=0 and A[s[top]]<A[i]:#not <=
                s.pop()
                top-=1
            if top>=0:
                R[i]=s[top]-i
            else:
                R[i]=n-i
            s.append(i)
            top+=1
        for i in range(n):
            L[i]*=R[i]
        return L
    def solve(self, A, B):
        freq = self.freq(A)
        #we just need the prods
        for i in range(len(A)):
            A[i] = self.divProd(A[i])
        #litle tough to understand
        keys =[]
        prev = 0
        values = []
        for i in sorted(zip(A,freq),reverse =True):
            keys.append(i[0])
            prev+=i[1]
            values.append(prev)
        #Quite unique new to me
        res = []
        for i in B:
            res.append(keys[bisect.bisect_left(values,i)])
        return res
            
        
        
        
        

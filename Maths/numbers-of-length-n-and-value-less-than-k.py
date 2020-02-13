class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer'
    def count(self, A, B, b, i):
        if i>=len(b) or B==0:
            return 1
        ans = 0
        c_max = int(b[i])
        for e in A:
            if e==0 and i==0 and B!=1:
                continue
            if e==c_max:
                if i==len(b)-1:
                    continue
                ans+=self.count(A, B-1, b, i+1)
                return ans
            if e>c_max:
                continue
            else:
                ans+=len(A)**(B-1)
        return ans
    def solve(self, A, B, C):
        c = len(str(C))
        a = len(A)
        ans = 0
        if B>c:
            return 0
        if B==c:
            return self.count(A,B,str(C),0)
        ans = 0
        for i in A:
            if i==0 and B!=1:
                continue
            if i==0 and i<C:
                #if only one digit -9
                ans+=1
            else:
                ans+=a**(B-1)
        return ans
            

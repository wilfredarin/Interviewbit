#https://www.interviewbit.com/problems/stringoholics/
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        
        def lps(pat):
            s = pat+pat
            i = s.find(s,1,-1)
            return len(pat) if i==-1 else len(pat[:i])
    
        def gcd(a,b):
            if b>a:
                a,b = b,a
            if b==0:return a
            return gcd(b,a%b)
            
        def lcm(a,b):
            return ((a*b)//gcd(a,b))
        
        
        ans = 1
        for s in A:
            n = lps(s)
            for i in range(1,2*n+1):
                if ((i*(i+1))//2)%n == 0:
                    ans =lcm(i,ans)
                    break
        return ans%(10**9+7)
                
            
        
        
       
        

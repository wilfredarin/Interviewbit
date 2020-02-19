class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        s = str(A)
        n = len(s)
        s = list(s)
        p = {}
        i = 1
        while i<=n:
            j=0
            while j+i<=n:
                o = s[j:j+i]
                u =1
                for q in o:
                  u*=int(q)  
                if u in p.keys():
                    return 0
                else:
                    p[u]=1
                j+=1
            i+=1
        return 1        
                
            
                
                
        

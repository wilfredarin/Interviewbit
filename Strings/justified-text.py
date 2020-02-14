class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        g = []
        s = 0
        ans =""
        res = []
        for word in A:
            if not word:
                continue
            if s+len(word)<=B:
                s+=len(word)+1
                g.append(word)
            else:
                t = B-(s-1)
                if len(g)==1:
                    res.append(g[0]+" "*t)
                else:
                    space = t//(len(g)-1)
                    left_space = t%(len(g)-1)
                    ans+=g.pop(0)
                    for e in g:
                        ans+=" "*(space+1)
                        if left_space>0:
                            ans+=" "
                            left_space-=1
                        ans+=e
                    res.append(ans)
                ans=""
                g = [word]
                s = len(word)+1
        if s:
            res.append(' '.join(g)+ " "*(B-s+1))
        return res
                
                
            

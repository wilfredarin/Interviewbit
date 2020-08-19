#https://www.interviewbit.com/problems/implement-strstr/
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    #KMP Algorithm 
    def strStr(self, A, B):
        #if either of them empty return -1
        if len(A)==0 or len(B)==0:
            return -1
        #if same return 0
        if A==B:
            return 0
        #function to create longest prefix sufix table for the pattern 
        def createLps(pat):
            n = len(pat)
            table = [0]*n
            cur = 1
            lps = 0
            while cur <n:
                if pat[cur] == pat[lps]:
                    lps+=1
                    table[cur] = lps
                    cur+=1
                else:
                    if lps==0:
                        table[cur] = 0
                        cur+=1
                    else:
                        lps = table[lps-1]
            return table
            
        #text index
        t_i =  0
        #pattern index
        p_i = 0
        table = createLps(B)
        while t_i<len(A):
            if p_i==len(B):
                return (t_i-p_i)
            if A[t_i]==B[p_i]:
                t_i+=1
                p_i+=1
            elif A[t_i]!=B[p_i]:
                if p_i==0:
                    t_i+=1
                else:
                    p_i = table[p_i-1]
        return -1
                
                
        
                    
            
            

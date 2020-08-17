class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        eow = -1
        sow = 0
        max_sow,max_eow = 0,0
        
        for i in A:
            eow+=1
            if i==0:
                if B==0:
                    if max_eow-max_sow<eow-sow:
                        max_eow = eow
                        max_sow = sow
                    while A[sow]!=0:
                        sow+=1
                    sow+=1 
                else:
                    B-=1 
        if max_eow-max_sow<eow-sow+1:
            return range(sow,eow+1)
        return range(max_sow,max_eow)
                    
                    
                    
                    

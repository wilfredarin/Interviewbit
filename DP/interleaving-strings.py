#https://www.interviewbit.com/problems/interleaving-strings/
class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        
  
        M = len(A) 
        N = len(B)  
      
       
        IL = [[0] * (N + 1) for i in range(M + 1)]  

        if ((M + N) != len(C)):  
            return 0
      
        for i in range(0, M + 1):  
            for j in range(0, N + 1): 
               
                if (i == 0 and j == 0):  
                    IL[i][j] = 1
      
                elif (i == 0):  
                    if (B[j - 1] == C[j - 1]):  
                        IL[i][j] = IL[i][j - 1]  
              
          
                elif (j == 0):  
                    if (A[i - 1] == C[i - 1]):  
                        IL[i][j] = IL[i - 1][j]  
                  
              
        
                elif (A[i - 1] == C[i + j - 1] and 
                      B[j - 1] == C[i + j - 1]):  
                    IL[i][j] = (IL[i - 1][j] or IL[i][j - 1])  
                
                elif (A[i - 1] == C[i + j - 1]):  
                    IL[i][j] = IL[i - 1][j]  
              
                elif  B[j - 1] == C[i + j - 1]:  
                    IL[i][j] = IL[i][j - 1]  
      
     
            
        if IL[-1][-1]:
            return 1
        else:
            return 0
        

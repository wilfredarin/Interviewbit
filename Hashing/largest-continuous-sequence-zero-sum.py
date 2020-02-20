class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        #Method Hash
        n = len(A)
        hash_map = {}
        cur_sum = 0
        max_len = 0
        start = None
        end = None
        for i in range(n):
            cur_sum+=A[i]
            if cur_sum==0 and i+1>max_len:
                start = 0
                end = i
                max_len = i+1
            elif cur_sum not in hash_map:
                hash_map[cur_sum] = i
            else:
                j = hash_map[cur_sum]
                if i-j>max_len:
                    start =j+1
                    end = i
                    max_len = i-j
        if start !=None:
            return A[start:end+1]
        else:
            return []
        
        #Method Brute
        """sum_array = 0
        max_len = -1
        array = [None,None]
        for i in range(n):
            sum_array = 0
            for j in range(i,n):
                sum_array+=A[j]
                if sum_array==0:
                    if max_len<(j+1-i):
                        array[1] = j
                        array[0] = i
                        max_len = j+1-i
        if array[1] is not None:
            return A[array[0]:array[1]+1]
        else:
            return []"""
        
                    
            
                
                
                
        
        

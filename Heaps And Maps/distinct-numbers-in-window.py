#https://www.interviewbit.com/problems/distinct-numbers-in-window
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        hash_map = {}
        dis_count = 0
        output = []
        n = len(A)
        for i in range(B):
            if A[i] in hash_map:
                hash_map[A[i]]+=1
            else:
                hash_map[A[i]]=1
                dis_count+=1
        output.append(dis_count)
        for j in range(B,n):
            #remove first
            if hash_map[A[j-B]]==1:
                dis_count-=1
            hash_map[A[j-B]]-=1
            #add new
            if A[j] in hash_map:
                if hash_map[A[j]]==0:
                    dis_count+=1
                hash_map[A[j]]+=1
            else:
                dis_count+=1
                hash_map[A[j]]=1
            output.append(dis_count)
        return output
                    
        
        

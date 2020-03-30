"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)

"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        hash_table = {}
        n = len(A)
        for i in range(n):
            if A[i] in hash_table:
                hash_table[A[i]].append(i)
            else:
                hash_table[A[i]] = [i]
        A = sorted(A)
        ans = 0
        index = n
        # 1 3 2 1 
        for i in range(n):
            if index>hash_table[A[i]][0]: #if index of this :first 1 in ex 3 1 2 1 
                #make this atleast first ocurence of it
                index = hash_table[A[i]][0]
            ans = max(ans,hash_table[A[i]][-1]-index)
            #we will here take las occurence of 1 in example 3 1 2 1
            #as we want it to be largest
        return ans
                
                
        
                
            
                
                
                
                
                
        

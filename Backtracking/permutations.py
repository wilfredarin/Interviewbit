"""

Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.


"""







import copy
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        n = len(A)
        def help_permute(array,res,curr):
            if len(curr)==len(array):
                res.append(copy.copy(curr))
            else:
                for i in range(n):
                    if array[i] not in curr:
                        curr.append(array[i])
                        help_permute(array,res,curr)
                        curr.pop()
        curr = []
        res = []
        help_permute(A,res,curr)
        return res
                        
                    
                        
                    
            

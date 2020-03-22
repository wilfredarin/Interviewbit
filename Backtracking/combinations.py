"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]

"""
import copy
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        array = []
        result = []
        ans = []
        for i in range(1,A+1):
            array.append(i)
        def help_combine(result,array,B,ans,index):
            if len(ans)==B:
                result.append(copy.copy(ans))
            for i in range(index,A):
                ans.append(array[i])
                help_combine(result,array,B,ans,i+1)
                ans.pop()
        help_combine(result,array,B,ans,0)
        return result
            


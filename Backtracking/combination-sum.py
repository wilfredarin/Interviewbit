"""

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.
Example, 
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
"""
import copy
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = set(A)
        A = sorted(list(A))
        result = ["sameer"]
        ans = []
        def help(index,result,ans,B):
            if sum(ans)>B:
                return
            if sum(ans)==B:
                if sorted(ans) != result[-1]:
                    result.append(sorted(copy.copy(ans)))
                return
            for i in range(index, len(A)):
                if sum(ans)+A[i]<=B:qa
                    ans.append(A[i])
                    help(i,result,ans,B)
                    ans.pop()
        help(0,result,ans,B)
        result = result[1:]
        return result
        
        
        
     

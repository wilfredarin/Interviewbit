"""

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]


"""


#Backtracking

import copy
def subsets(self,A):
        result = []
        temp = []
        index = 0
        def subset_helper(index, result, A, temp): 
            #this is important Call By reference copy.copy
            result.append(copy.copy(temp))
            #print(temp)
            for i in range(index,len(A)):
                temp.append(A[i])
                subset_helper(i+1,result,A,temp)
                #backtracking
                temp.pop()
            return    
        subset_helper(index, result, A, temp)
        return result
        
 """ 
 The set of subsets of {1} is {{}, {1}}
For {1, 2}, take {{}, {1}}, add 2 to each subset to get {{2}, {1, 2}} and take the union with {{}, {1}} to get {{}, {1}, {2}, {1, 2}}
Repeat till you reach n

 """
 def subsets(self, A):
        A.sort(reverse=True)
        results = [[]]
        while A:
            n = A.pop()
            temp = []
            for result in results:
                temp.append(result + [])
                temp.append(result + [n])
            results = temp
        results.sort()
        return results
 

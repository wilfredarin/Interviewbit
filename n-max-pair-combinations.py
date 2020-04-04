"""
Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6), 
9    (3+6),
9    (4+5),
8    (2+6)
"""
import heapq as hq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        A.sort(reverse=True)
        B.sort(reverse=True)
        result = []
        visited = set()
        heap = []
        hq.heappush(heap,(-(A[0]+B[0]),(0,0)))
        for i in range(n):
            sum ,(i,j) = hq.heappop(heap)
            result.append(-sum)
            index1 = (i+1,j)
            if i+1<n and index1 not in visited:
                hq.heappush(heap,(-(A[i+1]+B[j]),index1))
                visited.add(index1)
            index2 = (i,j+1)
            if j+1<n and index2 not in visited:
                hq.heappush(heap,(-(A[i]+B[j+1]),index2))
                visited.add(index2)
        return result
            

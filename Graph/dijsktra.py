#https://www.interviewbit.com/problems/dijsktra/
import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        q = [(0,C)]
        heapq.heapify(q)
        visited = [False]*(A)
        D = [-1]*A
        adj = [[] for x in range(A)]
        for x in B:
            adj[x[0]].append((x[1],x[2]))
            adj[x[1]].append((x[0],x[2]))
        while len(q):
            ele = heapq.heappop(q)
            if not visited[ele[1]]:
                visited[ele[1]]=True
                D[ele[1]] = ele[0]
                for nbr in adj[ele[1]]:
                    heapq.heappush(q,(ele[0]+nbr[1],nbr[0]))
        return D        
